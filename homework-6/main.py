import datetime

import calendar

day = int(input("Введіть день народження: "))

month = int(input("Введіть місяць свого народження: "))

if not( 1 <= month <= 12):
    print("Помилка. Неправильний день чи місяць.")
    exit()

max_day = calendar.monthrange(2020, month)[1]

if not(1 <= day <= max_day and 1 <= month <= 12):
    print("Помилка. Неправильний день чи місяць.")
    exit()

user_date = datetime.date(2020, month, day)

if datetime.date(2020, 1, 21) <= user_date <= datetime.date(2020, 2, 18):
    print("\n Ви Водолій \n")
    print("На представників знаків повітряної стихії — Близнят, Терезів і Водолія \nЧекає динамічний рік,який сприятиме проявам ініціативи в комунікації й інтелектуальній діяльності. \nРушійними силами 2023-го стануть ваше натхнення, легкість і життєлюбність. А експертність, здатність \nдо компромісів і підтримка надійних партнерів допоможуть досягти задуманого. \nЦього року ви — активні стратеги.")
elif datetime.date(2020, 2, 19) <= user_date <= datetime.date(2020, 3, 20):
    print("\n Ви Риби \n")
    print("Представникам знаків Води — Рака, Скорпіона, Риб \nРік нагадуватиме контрастний душ: то підноситиме догори і спонукатиме до відкритості та творчості, \nто занурюватиме на звичні глибини, даруючи опору та спокій. Цього року ви — завбачливі ентузіасти. \nВаші уява та інтуїція будуть на висоті. Якщо у вас є заповітна мрія або ціль, саме ці здібності допоможуть швидше наблизитися до неї.")
elif datetime.date(2020, 3, 21) <= user_date <= datetime.date(2020, 4, 20):
    print("\n Ви Овен \n")
    print("Представникам вогняних знаків — Овнам, Левам і Стрільцям  \nУ 2023 році випаде щасливий білет. Ваші ініціативність, ентузіазм, лідерські якості матимуть великий попит, \nа ідеї надихатимуть інших на видатні досягнення. Цього року ви — допитливі мандрівники, що відкривають \nнові світи й тестують себе на якість взаємин з оточенням, на витривалість і вміння досягати мети.")
elif datetime.date(2020, 4, 21) <= user_date <= datetime.date(2020, 5, 21):
    print("\n Ви Телець \n")
    print("'Дайте мені точку опертя, і я зрушу світ!' — гасло представників знаків Землі на 2023 рік, \nякий усіма способами спонукатиме послабити зайву обережність й опанувати продуктивну активність. \nСкрізь, де ви вкладатимете сили й час, є шанс отримати матеріальний результат і прокачати такі важливі \nдля вас суперздібності, як терпіння, працьовитість, стійкість, надійність. \nЦього року представники знаків Телець, Діва, Козоріг — сміливі реалісти.")
elif datetime.date(2020, 5, 22) <= user_date <= datetime.date(2020, 6, 21):
    print("\n Ви Близнята \n")
    print("На представників знаків повітряної стихії — Близнят, Терезів і Водолія \nЧекає динамічний рік,який сприятиме проявам ініціативи в комунікації й інтелектуальній діяльності. \nРушійними силами 2023-го стануть ваше натхнення, легкість і життєлюбність. А експертність, здатність \nдо компромісів і підтримка надійних партнерів допоможуть досягти задуманого. \nЦього року ви — активні стратеги.")
elif datetime.date(2020, 6, 22) <= user_date <= datetime.date(2020, 7, 22):
    print("\n Ви Рак \n")
    print("Представникам знаків Води — Рака, Скорпіона, Риб \nРік нагадуватиме контрастний душ: то підноситиме догори і спонукатиме до відкритості та творчості, \nто занурюватиме на звичні глибини, даруючи опору та спокій. Цього року ви — завбачливі ентузіасти. \nВаші уява та інтуїція будуть на висоті. Якщо у вас є заповітна мрія або ціль, саме ці здібності допоможуть швидше наблизитися до неї.")
elif datetime.date(2020, 7, 23) <= user_date <= datetime.date(2020, 8, 21):
    print("\n Ви Лев \n")
    print("Представникам вогняних знаків — Овнам, Левам і Стрільцям  \nУ 2023 році випаде щасливий білет. Ваші ініціативність, ентузіазм, лідерські якості матимуть великий попит, \nа ідеї надихатимуть інших на видатні досягнення. Цього року ви — допитливі мандрівники, що відкривають \nнові світи й тестують себе на якість взаємин з оточенням, на витривалість і вміння досягати мети.")
elif datetime.date(2020, 8, 22) <= user_date <= datetime.date(2020, 9, 23):
    print("\n Ви Діва \n")
    print("'Дайте мені точку опертя, і я зрушу світ!' — гасло представників знаків Землі на 2023 рік, \nякий усіма способами спонукатиме послабити зайву обережність й опанувати продуктивну активність. \nСкрізь, де ви вкладатимете сили й час, є шанс отримати матеріальний результат і прокачати такі важливі \nдля вас суперздібності, як терпіння, працьовитість, стійкість, надійність. \nЦього року представники знаків Телець, Діва, Козоріг — сміливі реалісти.")
elif datetime.date(2020, 9, 24) <= user_date <= datetime.date(2020, 10, 23):
    print("\n Ви Терези \n")
    print("На представників знаків повітряної стихії — Близнят, Терезів і Водолія \nЧекає динамічний рік,який сприятиме проявам ініціативи в комунікації й інтелектуальній діяльності. \nРушійними силами 2023-го стануть ваше натхнення, легкість і життєлюбність. А експертність, здатність \nдо компромісів і підтримка надійних партнерів допоможуть досягти задуманого. \nЦього року ви — активні стратеги.")
elif datetime.date(2020, 10, 24) <= user_date <= datetime.date(2020, 11, 22):
    print("\n Ви Скорпіон \n")
    print("Представникам знаків Води — Рака, Скорпіона, Риб \nРік нагадуватиме контрастний душ: то підноситиме догори і спонукатиме до відкритості та творчості, \nто занурюватиме на звичні глибини, даруючи опору та спокій. Цього року ви — завбачливі ентузіасти. \nВаші уява та інтуїція будуть на висоті. Якщо у вас є заповітна мрія або ціль, саме ці здібності допоможуть швидше наблизитися до неї.")
elif datetime.date(2020, 11, 23) <= user_date <= datetime.date(2020, 12, 21):
    print("\n Ви Стрілець \n")
    print("Представникам вогняних знаків — Овнам, Левам і Стрільцям  \nУ 2023 році випаде щасливий білет. Ваші ініціативність, ентузіазм, лідерські якості матимуть великий попит, \nа ідеї надихатимуть інших на видатні досягнення. Цього року ви — допитливі мандрівники, що відкривають \nнові світи й тестують себе на якість взаємин з оточенням, на витривалість і вміння досягати мети.")
elif datetime.date(2020, 12, 22) <= user_date <= datetime.date(2020, 1, 20):
    print("\n Ви Козеріг \n")
    print("'Дайте мені точку опертя, і я зрушу світ!' — гасло представників знаків Землі на 2023 рік, \nякий усіма способами спонукатиме послабити зайву обережність й опанувати продуктивну активність. \nСкрізь, де ви вкладатимете сили й час, є шанс отримати матеріальний результат і прокачати такі важливі \nдля вас суперздібності, як терпіння, працьовитість, стійкість, надійність. \nЦього року представники знаків Телець, Діва, Козоріг — сміливі реалісти.")










