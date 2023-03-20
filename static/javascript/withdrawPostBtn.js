document.getElementById('withdrawPostBtn')?.addEventListener('click', async function () {
    if (confirm("Are you sure you want to withdraw this post?")) {
        const csrfToken = document.getElementById('csrf-token').value;
        const itemId = this.dataset.itemId;
        const response = await fetch(`/item/${itemId}/withdraw/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
        });
        const data = await response.json();
        if (data.status === 'success') {
            alert('Post withdrawn successfully');
            window.location.reload();
        } else {
            alert(data.message || 'An error occurred');
        }
    }
});