class Translation(object):
    START_TEXT = """Hi!
Cảm ơn bạn đã sử dụng tôi 😬
Nhập Số điện thoại Telegram của bạn để nhận APP-ID từ my.telegram.org

/start ở bất kỳ giai đoạn nào để nhập lại thông tin chi tiết của bạn"""
    AFTER_RECVD_CODE_TEXT = """Tôi hiểu rồi!
bây giờ vui lòng gửi mã Telegram mà bạn đã nhận được từ Telegram!

/start ở bất kỳ giai đoạn nào để nhập lại chi tiết của bạn"""
    BEFORE_SUCC_LOGIN = "đã nhận mã. Trang web cóp nhặt ..."
    ERRED_PAGE = "một cái gì đó sai. không lấy được id ứng dụng. \n\n@@Kuri69"
    CANCELLED_MESG = "Tạm biệt! Vui lòng lại /start cuộc trò chuyện với bot"
    IN_VALID_CODE_PVDED = "xin lỗi, nhưng đầu vào có vẻ không phải là mã Đăng nhập Web Telegram hợp lệ"
    IN_VALID_PHNO_PVDED = "xin lỗi, nhưng đầu vào có vẻ không phải là số điện thoại hợp lệ"
