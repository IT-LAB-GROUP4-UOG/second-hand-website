document.getElementById('buyBtn')?.addEventListener('click', async function () {
    if (confirm("Are you sure you want to buy this item?")) {
        const csrfToken = document.getElementById('csrf-token').value;
        const itemId = this.dataset.itemId;
        const response = await fetch(`/item/${itemId}/buy/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
        });
        const data = await response.json();
        if (data.status === 'success') {
            alert('Item purchased successfully');
            window.location.href = this.dataset.orderDetailUrl.replace('0', data.order_id);
        } else {
            alert(data.message || 'An error occurred');
        }
    }
});