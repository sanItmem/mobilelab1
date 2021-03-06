from fpdf import FPDF
import sys 
import os
from Мобилки1 import in_call, out_call, sms, call_duration, k_in, k_out, k_sms
from Мобилки2 import mbyte, k, internet
#создание
pdf = FPDF()
pdf.add_page()

#первая табличка
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.1)
pdf.line(12, 15, 12, 44)
pdf.line(12, 28, 185, 28)
pdf.line(12, 32, 106, 32)
pdf.line(106, 15, 106, 44)
pdf.line(123, 15, 123, 44)
pdf.line(61, 28, 61, 32)
pdf.line(185, 15, 185, 44)
pdf.line(106, 20, 123, 20)
pdf.line(12, 15, 185, 15)
pdf.line(12, 44, 185, 44)
#текст первой таблички
pdf.add_font('DejaVu', '', 'C:/Users/prova/AppData/Local/Microsoft/Windows/Fonts/DejaVuSansCondensed.ttf', uni=True)
pdf.set_font("DejaVu", size = 9)
pdf.cell(66, 15, txt = "АО ''Хороший банк'' г. Санкт-Петербург ", ln = 1, align = "C")
pdf.cell(31, 2, txt = "Банк получателя", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 11)
pdf.cell(200, -18, txt = "БИК", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(245, 18, txt = "044547195", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(201, -10, txt = "Сч. №", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(267, 10, txt = "91781647143416878513", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(201, 6, txt = "Сч. №", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(267, -6, txt = "88904667314223261804", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(12, 6, txt = "ИНН", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(46, -6, txt = "6577203339", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(110, 6, txt = "КПП", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 10)
pdf.cell(144, -6, txt = "933302775", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(46, 14, txt = "ООО ''Хорошая компания'' ", ln = 1, align = "C")
pdf.set_font("DejaVu", size =9)
pdf.cell(23, 1, txt = "Получатель", ln = 1, align = "C")
#линия "Счет..."
pdf.set_line_width(0.5)
pdf.line(12, 60, 185, 60)
pdf.set_font("DejaVu", size = 14)
pdf.cell(105, 22, txt = "Счет на оплату № 79 от 27 апреля 2020 г.", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(175, 3, txt = "Поставщик           ООО ''ХОРОШАЯ КОМПАНИЯ'', ИНН 6577203339, КППП 933302775, 197101, г. Санкт-Петербург,", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(101, 3, txt = "(Исполнитель):       ул. Ординарная, д.21, тел.: +7(967)229-87-45", ln = 1, align = "C")
pdf.set_font("DejaVu", size =9)
pdf.cell(162, 15, txt = "Покупатель           ООО ''Лучший бизнес'', ИНН 9928922161, КПП 674321686,197101, г. Санкт-Петербург,", ln = 1, align = "C")
pdf.set_font("DejaVu", size =9)
pdf.cell(112, -8, txt = "(Заказчик):             ул. Большая Монетная, д.20, тел.: +7(812)232-43-02 ", ln = 1, align = "C")
pdf.set_font("DejaVu", size =9)
pdf.cell(72, 25, txt = "Основание:            № 45708761 от 18.04.2015", ln = 1, align = "C")
#вторая табличка
pdf.set_line_width(0.5)
pdf.line(12, 95, 12, 120)
pdf.line(12, 95, 185, 95)
pdf.line(12, 120, 185, 120)
pdf.line(185, 95, 185, 120)
pdf.set_line_width(0.1)
pdf.line(12, 100, 185, 100)
pdf.line(12, 106, 185, 106)
pdf.line(12, 113, 185, 113)
pdf.line(20, 95, 20, 120)
pdf.line(106, 95, 106, 120)
pdf.line(135, 95, 135, 120)
pdf.line(155, 95, 155, 120)
pdf.set_font("DejaVu", size = 9)
pdf.cell(12, -9, txt = "№", ln = 1, align = "C")
pdf.cell(12, 20, txt = "1", ln = 1, align = "C")
pdf.cell(12, -6, txt = "2", ln = 1, align = "C")
pdf.cell(12, 19, txt = "3", ln = 1, align = "C")
pdf.cell(100, -57, txt = "Товары(услуги)", ln = 1, align = "C")
pdf.cell(39, 68, txt = "Телефония", ln = 1, align = "C")
pdf.cell(30, -54, txt = "СМС", ln = 1, align = "C")
pdf.cell(38, 67, txt = "Интернет", ln = 1, align = "C")
pdf.cell(220, -104, txt = "Кол-во", ln = 1, align = "C")
pdf.cell(269, 104, txt = "Цена", ln = 1, align = "C")
pdf.cell(319, -104, txt = "Сумма", ln = 1, align = "C")
pdf.cell(220, 114, txt = str(call_duration * 2), ln = 1, align = "C")
pdf.cell(220, -101, txt = str(sms), ln = 1, align = "C")
pdf.cell(220, 115, txt = str(round(mbyte, 2)), ln = 1, align = "C")
pdf.set_font("DejaVu", size = 7)
pdf.cell(270, -145, txt = str(k_in), ln = 1, align = "C")
pdf.cell(262, 145, txt = "Вх.:", ln = 1, align = "C")
pdf.cell(270, -140, txt = str(k_out), ln = 1, align = "C")
pdf.cell(260, 140, txt = "Вых.:", ln = 1, align = "C")
pdf.set_font("DejaVu", size = 9)
pdf.cell(270, -129, txt = str(k_sms), ln = 1, align = "C")
pdf.cell(270, 143, txt = str(k), ln = 1, align = "C")
pdf.cell(319,-170, txt = str(in_call + out_call), ln = 1, align = "C")
pdf.cell(319, 183, txt = str(sms), ln = 1, align = "C")
pdf.cell(319, -169, txt = str(round(internet, 2)), ln = 1, align = "C")
summa = in_call + out_call + sms + internet
pdf.cell(310, 188, txt = "Итого:   ", ln = 1, align = "C")
pdf.cell(340, -188, txt = str(round(summa, 2)), ln = 1, align = "C")
pdf.cell(294, 198, txt = "В том числе НДС:   ", ln = 1, align = "C")
nds = summa * 0.2
pdf.cell(341, -198, txt = str(round(nds, 2)), ln = 1, align = "C")
pdf.cell(296, 208, txt = "Всего к оплате:   ", ln = 1, align = "C")
pdf.cell(340, -208, txt = str(round(summa, 2)), ln = 1, align = "C")
pdf.cell(70, 218, txt = "Всего наименований 3, на сумму 28,63 руб.", ln = 1, align = "C")
pdf.cell(80, -208, txt = "Двадцать восемь рублей шестьдесят три копейки", ln = 1, align = "C")
pdf.cell(20, 223, txt = "Внимание!", ln = 1, align = "C")
pdf.cell(113, -215, txt = "Оплата данного счета означает согласие с условиями поставки товара.", ln = 1, align = "C")
pdf.cell(161, 223, txt = "Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.", ln = 1, align = "C")
pdf.cell(182, -215, txt = "Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и паспорта.", ln = 1, align = "C")
#линия 2
pdf.set_line_width(0.5)
pdf.line(12, 172, 185, 172)
#подписи
pdf.set_line_width(0.1)
pdf.line(41, 181, 108, 181)
pdf.line(137, 181, 185, 181)
pdf.output("bill.pdf")
