import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # تحسب عدد الكلمات الموجودة في كل رسالة محددة مسبقًا
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # تحسب النسبة المئوية للكلمات التي تم التعرف عليها في رسالة المستخدم
    percentage = float(message_certainty) / float(len(recognised_words))

    #يتحقق من وجود الكلمات المطلوبة في السلسلة
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # يجب أن تحتوي على الكلمات المطلوبة ، أو أن تكون إجابة واحدة
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # يبسط إنشاء الاستجابة / يضيفها إلى الإختصار
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    # ________________________________________________________________________________________ استجابات
    response('ياهلابك !', ['مرحبا','هلا', 'هلاوالله'], single_response=True)
    response('الله يحفظك', ['سلام', 'مع السلامه', 'اشوفك بعدين'], single_response=True)
    response('انا والله بخير كيف صحتك انت ؟ ', ['كيف', 'حالك ؟'], required_words=['كيف'])
    response('الله يديم عليك ', ['الحمدلله', 'بخير'], required_words=['الحمدلله'])
    response('انت مرحب بك بأي وقت !', ['شكرا', 'مشكور'], single_response=True)
    response('شكرا لك !', ['يا ', 'اهلا ', 'وسهلا '], required_words=['اهلا ', 'وسهلا '])


    # استجابات أطول
    response(long.R_ADVICE, ['اعطي', 'نصيحة'], required_words=['نصيحة'])
    response(long.R_EATING, ['ماذا', 'انت', 'تأكل '], required_words=['انت', 'تأكل'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# تستخدم للحصول على الرد
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# اختبار نظام الاستجابة
while True:
    print('Bot: ' + get_response(input('You: ')))