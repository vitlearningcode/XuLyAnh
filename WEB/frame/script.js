/* script.js - Xử lý tương tác cho website */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- CHỨC NĂNG 1: THÊM VÀO GIỎ (Trang Thực đơn) ---
    // Tìm tất cả các nút có class 'btn-add'
    const addButtons = document.querySelectorAll('.btn-add');
    
    if (addButtons.length > 0) {
        addButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Lấy thông tin món ăn từ thẻ cha chứa nút bấm
                const itemInfo = e.target.parentElement;
                const itemName = itemInfo.querySelector('.name').innerText;
                const itemPrice = itemInfo.querySelector('.price').innerText;
                
                // Hiển thị thông báo (thay vì xử lý backend phức tạp)
                alert(`Đã thêm món: ${itemName} (${itemPrice}) vào giỏ hàng!`);
            });
        });
    }

    // --- CHỨC NĂNG 2: GỬI LIÊN HỆ (Trang Liên hệ) ---
    // Tìm form trong trang
    const contactForm = document.querySelector('form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', (event) => {
            // Ngăn chặn trang web reload lại
            event.preventDefault();
            
            // Lấy giá trị từ các ô input
            const inputs = contactForm.querySelectorAll('input, textarea');
            let hasEmpty = false;
            
            // Kiểm tra sơ bộ xem có ô nào để trống không
            inputs.forEach(input => {
                if (!input.value.trim()) hasEmpty = true;
            });

            if (hasEmpty) {
                alert('Vui lòng điền đầy đủ thông tin!');
            } else {
                alert('Cảm ơn bạn đã gửi tin nhắn! Chúng tôi sẽ phản hồi sớm nhất.');
                contactForm.reset(); // Xóa trắng form sau khi gửi
            }
        });
    }
});