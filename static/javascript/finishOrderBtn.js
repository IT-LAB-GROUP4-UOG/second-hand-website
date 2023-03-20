document.getElementById('finishOrderBtn')?.addEventListener('click', async function () {
    if (confirm("Are you sure you want to finish this order?")) {
        const csrfToken = document.getElementById('csrf-token').value;
        const orderId = this.dataset.orderId;
        const response = await fetch(`/order/${orderId}/finish/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
        });
        const data = await response.json();
        if (data.status === 'success') {
            alert('Order finished successfully');
            window.location.reload();
        } else {
            alert(data.message || 'An error occurred');
        }
    }
});