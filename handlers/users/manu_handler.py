from keyboards.default.tanlov import menu_button
from keyboards.default.menu import menu_buttons
from loader import dp,bot
from aiogram import types
from states.ishstate import Ishkerak
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Ishjoyi kerak")
async def ish_joyi(message: types.Message):
    taxt=f"Ish joyi topish uchun ariza berish"
    taxt+=f"Hozir sizga birnecha savollar beriladi. "
    taxt+=f"Har biriga javob bering. "
    taxt+=f"Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va "
    taxt+=f"arizangiz Adminga yuboriladi."
    await message.answer(taxt)
    await message.answer("<b>Ism, familiyangizni kiriting?</b>")
    await Ishkerak.ism_familya.set()

@dp.message_handler(state=Ishkerak.ism_familya)
async def ism_familyasi(message: types.Message, state: FSMContext):
    ism_familya=message.text
    await state.update_data(
        {
            "ism_familya": ism_familya,
        }
    )
    await Ishkerak.yosh.set()
    await message.answer("""<b>🕑 Yosh: 
                        Yoshingizni kiriting?
                        Masalan, 19</b>
                                            """)
@dp.message_handler(state=Ishkerak.yosh)
async def yosh_state(message: types.Message, state: FSMContext):
    yoshi=message.text
    await state.update_data(
        {
            "yoshi": yoshi,
        }
    )
    await Ishkerak.texno.set()
    text=f"📚 Texnologiya:\n\n"
    text+=f"Talab qilinadigan texnologiyalarni kiriting?\n"
    text+=f"Texnologiya nomlarini vergul bilan ajrating. Masalan,\n\n"
    text+=f"<i>Java, C++, C#, Python</i>"
    await message.answer(text)
@dp.message_handler(state=Ishkerak.texno)
async def texno_state(message: types.Message, state: FSMContext):
    texno=message.text
    await state.update_data(
        {
            "texno": texno,
        }
    )
    await Ishkerak.aloqa.set()
    tel=f"📞 Aloqa: "
    tel+=f"Bog`lanish uchun raqamingizni kiriting?"
    tel+=f"Masalan, +998 90 123 45 67"
    await message.answer(tel)
@dp.message_handler(state=Ishkerak.aloqa)
async def aloqa_state(message: types.Message, state: FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            "aloqa": aloqa,
        }
    )
    await Ishkerak.hudud.set()
    joy=f"🌐 Hudud:"
    joy+=f"Qaysi hududdansiz?"
    joy+=f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."
    await message.answer(joy)
@dp.message_handler(state=Ishkerak.hudud)
async def hudud_state(message: types.Message, state: FSMContext):
    hudud=message.text
    await state.update_data(
        {
            "hudud": hudud,
        }
    )
    await Ishkerak.narx.set()
    som=f"💰 Narxi:"
    som+=f"Tolov qilasizmi yoki Tekinmi?"
    som+=f"Kerak bo`lsa, Summani kiriting?"
    await message.answer(som)
@dp.message_handler(state=Ishkerak.narx)
async def narx_state(message: types.Message, state: FSMContext):
    narx=message.text
    await state.update_data(
        {
            "narx": narx,
        }
    )
    await Ishkerak.kasbi.set()
    ish=f"👨🏻‍💻 Kasbi: "
    ish+=f"Ishlaysizmi yoki o`qiysizmi?"
    ish+=f"Masalan, Talaba"
    await message.answer(ish)
@dp.message_handler(state=Ishkerak.kasbi)
async def kasbi_state(message: types.Message, state: FSMContext):
    kasbi=message.text
    await state.update_data(
        {
            "kasbi": kasbi,
        }
    )
    await Ishkerak.murojat_vaqti.set()
    murojat=f"🕰 Murojaat qilish vaqti: "
    murojat+=f"Qaysi vaqtda murojaat qilish mumkin?"
    murojat+=f"Masalan, 9:00 - 18:00"
    await message.answer(murojat)
@dp.message_handler(state=Ishkerak.murojat_vaqti)
async def murojat_state(message: types.Message, state: FSMContext):
    murojat=message.text
    await state.update_data(
        {
            "murojat": murojat,
        }
    )
    await Ishkerak.maqsad.set()
    maqsad=f"🔎 Maqsad: "
    maqsad+=f"Maqsadingizni qisqacha yozib bering."
    await message.answer(maqsad)
@dp.message_handler(state=Ishkerak.maqsad)
async def maqsad_state(message: types.Message, state: FSMContext):
    maqsad=message.text
    await state.update_data(
        {
            "maqsad": maqsad,
        }
    )
    await Ishkerak.maqsad.set()
    user_data = await state.get_data()
    ism_familiya = user_data.get('ism_familya')
    yosh = user_data.get('yoshi')
    texno = user_data.get('texno')
    aloqa = user_data.get('aloqa')
    hudud = user_data.get('hudud')
    narxi = user_data.get('narx')
    kasbi = user_data.get('kasbi')
    murojat = user_data.get('murojat')
    maqsad = user_data.get('maqsad')

    text = f"Ish joyi kerak\n\n"
    text += f"👨‍💼 Xodim:{ism_familiya}\n"
    text += f"🕑 Yosh:{yosh}\n"
    text += f"📚 Texnologiya:{texno}\n"
    text += f"🇺🇿 Telegram:{message.from_user.username}\n"
    text += f"📞 Aloqa:{aloqa}\n"
    text += f"🌐 Hudud:{hudud}\n"
    text += f"💰 Narxi:{narxi}\n"
    text += f"👨🏻‍💻 Kasbi:{kasbi}\n"
    text += f"🕰 Murojaat vaqti:{murojat}\n"
    text += f"🔎 Maqsad:{maqsad}\n"

    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=menu_button)


@dp.message_handler(text="Ha")
async def ha_choice(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    text = f"Ish joyi kerak:\n\n👨‍💼 Xodim: {user_data.get('ism_familya')}\n🕑 Yosh: {user_data.get('yoshi')}\n" \
           f"📚 Texnologiya: {user_data.get('texno')}\n📞 Aloqa: {user_data.get('aloqa')}\n🌐 Hudud: {user_data.get('hudud')}\n" \
           f"💰 Narxi: {user_data.get('narx')}\n👨🏻‍💻 Kasbi: {user_data.get('kasbi')}\n🕰 Murojaat vaqti: {user_data.get('murojat')}\n" \
           f"🔎 Maqsad: {user_data.get('maqsad')}"
    # Admin chat ID'sini aniqlang
    admin_chat_id = 7126357860
    await bot.send_message(admin_chat_id,text)
    await message.answer("So'rov adminga yuborildi.")
    # State ni tugatish
    await state.finish()




@dp.message_handler(text="yo'q")
async def yoq_choice(message: types.Message, state: FSMContext):
    await message.answer("So'rov bekor qilindi.")
    await state.finish()


@dp.message_handler(text="Sherik kerak")
async def sherik(message: types.Message):
    await message.answer("Bu 2qism tayorlanmoqda .....")


@dp.message_handler(text="Hodim kerak")
async def hodim(message: types.Message):
    await message.answer("Bu 3qism tayorlanmoqda .....")

@dp.message_handler(text="Ustoz kerak")
async def ustoz(message: types.Message):
    await message.answer("Bu 4qism tayorlanmoqda .....")



@dp.message_handler(text="shogird kerak")
async def shogir(message: types.Message):
    await message.answer("Bu 5qism tayorlanmoqda .....")



