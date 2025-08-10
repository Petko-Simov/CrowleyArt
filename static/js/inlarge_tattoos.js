document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('tattoo-modal');
    const modalImg = document.getElementById('modal-img');
    const titleEl = document.getElementById('modal-title');
    const styleEl = document.getElementById('modal-style');
    const priceEl = document.getElementById('modal-price');
    const close = document.querySelector('.tattoo-modal-close');

    // helper to open modal card info
    function openCard(card) {
        const img = card.querySelector('img');
        let title = card.querySelector('.card-title')?.textContent?.trim();
        let style = card.querySelectorAll('.card-text')[0]?.textContent?.trim();
        let price = card.querySelectorAll('.card-text')[1]?.textContent?.trim();

        if (!title) title = card.dataset.title || '';
        if (!style) style = card.dataset.style || '';
        if (!price) price = card.dataset.price || '';

        modalImg.src = img?.dataset.full || img?.src || '';
        titleEl.textContent = title;
        styleEl.textContent = style;
        priceEl.textContent = price;

        modal.classList.add('open');
    }

    document.querySelectorAll('.tattoo-card').forEach(card => {
        card.addEventListener('click', () => {

            console.log('USER_IS_AUTH:', window.USER_IS_AUTH, 'LOGIN_PROMPT_URL:', window.LOGIN_PROMPT_URL);

            const isAuth = window.USER_IS_AUTH === true || window.USER_IS_AUTH === 'true';

            if (!isAuth) {
                const current = window.location.pathname + window.location.search;
                const next = encodeURIComponent(current);
                const loginPromptUrl = window.LOGIN_PROMPT_URL || '/gallery/please-login/'; // fallback
                // debug
                console.log('Redirecting to login prompt with next=', current);
                window.location.href = `${loginPromptUrl}?next=${next}`;
                return;
            }

            openCard(card);
        });
    });

    const closeModal = () => {
        if (modal) {
            modal.classList.remove('open');
            modalImg.src = '';
        }
    };

    close?.addEventListener('click', closeModal);
    modal?.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
});
