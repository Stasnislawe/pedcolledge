function togglePopup(event) {
        const popup = event.target.nextElementSibling;
        const allPopups = document.querySelectorAll('.popup');

        // Скрыть все всплывающие окна
        allPopups.forEach(p => {
            if (p !== popup) p.style.display = 'none';
        });
        
        // Переключить текущее всплывающее окно
        if (popup.style.display === 'none' || popup.style.display === '') {
            popup.style.display = 'flex';
        } else {
            popup.style.display = 'none';
        }
        
        // Добавляем обработчик для закрытия всплывающего окна при клике вне
        document.addEventListener('click', function hidePopup(e) {
            if (!event.target.closest('td') || e.target === popup) {
                popup.style.display = 'none';
                document.removeEventListener('click', hidePopup);
            }

            // Открытое всплывающее окно
            if (popup.style.display !== 'none') {
                popup.style.display = 'none';
                document.removeEventListener('click', hidePopup);
            }
        });
        
        event.stopPropagation(); // Остановить событие клика от дальнейшей обработки
    }