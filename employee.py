import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import re


load_dotenv()
here = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(here, 'profile_structure.json')
client = OpenAI()
model_name = 'gpt-4o'


def extract_json_from_string(text: str):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        json_string = match.group(0)
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return None
    return None


def is_complete(conversation_history, profile_structure):
    prompt = f'''
    
    {json.dumps(profile_structure)} این ساختار مورد نیاز پروفایل است.
    {json.dumps(conversation_history)} تاریخچه ی گفتگو با کاربر است.
    با توجه به تاریخچه، آیا تمام بخش‌های اصلی پروفایل (مانند اطلاعات شخصی، حداقل یک تجربه کاری، و مهارت‌ها) به طور معقولی پر شده‌اند؟
    فقط و فقط با یک کلمه پاسخ بده: 'بله' یا 'خیر'.
    '''

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "شما دستیار هوشمندی هستی که وظیفه ات این است که تشخیص دهی پروفایل کاربر کامل شده است یا خیر."
                },
                {
                  "role": "user",
                  "content": prompt
                },
            ],
            max_tokens=3,
            temperature=0,
        )

        answer = response.choices[0].message.content.strip()
        return "بله" in answer
    except Exception as e:
        return False


def start_employee_journey():
    print('حالت کارمند با دریافت رزومه انتخاب شد.')
    profile_data = dict()
    your_full_name = input('سلام. خوش آمدید. لطفا اسم خود را به صورت کامل وارد فرمایید: ')

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    system_prompt = '''
    دستیار هوشمندی هستی که بیش از ۲۰ سال سابقه ی ایجاد پروفایل از روی رزومه و سوال پرسیدن از کاربر در مورد حرفه اش داری.
    '''

    user_prompt = f'''
    سوالاتی از کاربر بپرس راجع به شغلش و رفته رفته عیقتر شو در سوالات تا مطالب مفیدی از کاربر دستگیرت شود.
    مثلا بپرس مهمترین دستاوردت در آخرین جایی که کار کردی (شرکت x) چی بود؟
    مطمئن شو هر سوالی رااز هر کاربر فقط یک بار بپرسی.
    مطمئن شو ساختاری مثل {data} را با اطلاعاتی که از کاربر می گیری پر می کنی.
    نام کاربر {your_full_name} است.
    در هر مرحله یک سوال بپرس.
    به عنوان آخرین سوال بپرس اگه نکته یا موردی هست که در سوالات گفته نشده و دوست داشته بگه چیه؟
    '''

    message_list = [
        {
            "role": "system",
            "content": system_prompt,
        },

        {
            "role": "user",
            "content": user_prompt,
        }
    ]

    while True:
        # conversational agent
        agent = client.chat.completions.create(
            model=model_name,
            messages=message_list,
            max_tokens=100,
            temperature=0.7,
        )
        agent_response = agent.choices[0].message.content
        print("دستیار: ", agent_response)
        user_answer = input("پاسخ شما: ")
        message_list.append({"role": "assistant", "content": agent_response})
        message_list.append({"role": "user", "content": user_answer})

        # checking if all needed data catched.
        if is_complete(message_list, data):
            print('اطلاعات کافی از شما جمع آوری شد. با تشکر از شما. این گفتگو به پایان رسید')
            break

    # expert agent for extracting data from conversation.
    prompt = f'''
    شما یک پروفایل ساز از روی تاریخچه ی مکالمات هستی. تاریخچه ی گفتگو را با دقت بسیار بررسی و تحلیل کن و اطلاعات آن را در قالب json استخراج کن.
    ساختار مورد نظر این است: {data}
    خروجی تو باید یک آبجکت json معتبر باشد و هیچ کلمه یا متن اضافی مثل (مثل "حتما, این هم از JSON شما:") در پاسخ خود نیاور
    حتما مطمئن شو خروجیت فقط json object هست.
    '''

    message_list.append({
        "role": "user",
        "content": prompt
    })
    expert_agent = client.chat.completions.create(
        model=model_name,
        messages=message_list,
        max_tokens=500,
        temperature=0
    )

    raw_resp = expert_agent.choices[0].message.content
    try:
        extracted_data = extract_json_from_string(raw_resp)
        profile_data.update(extracted_data)
        file_name = f"{your_full_name.replace(' ', '_')}.json"
        profile_path = os.path.join(here, 'profiles', file_name)
        with open(profile_path, 'w', encoding='utf-8') as file:
            json.dump(profile_data, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print('خطای غیر منتظره رخ داده است:')
