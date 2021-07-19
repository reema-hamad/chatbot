import random

R_EATING = "أنا لا أحب أكل أي شيء لأنني روبوت !"
R_ADVICE = "لو كنت مكانك ، كنت سأذهب إلى الإنترنت وأكتب بالضبط ما كتبته هنا!"


def unknown():
    response = ["ممكن توضح لي هذا بصياغة ثانيه ؟ ",
                "...",
                "تبدو صحيحه .",
                "وش تعني مافهمت ؟"][
        random.randrange(4)]
    return response