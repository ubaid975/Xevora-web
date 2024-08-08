document.querySelectorAll('.read-more').forEach(function(button) {
    button.addEventListener('click', function() {
        var blogContentId = 'blog-content-' + this.getAttribute('data-id');
        var blogContent = document.getElementById(blogContentId);

        if (blogContent.style.display === 'none' || !blogContent.style.display) {
            blogContent.style.display = 'block';
            this.innerHTML = 'Read Less';
            this.classList.add('clicked');
        } else {
            blogContent.style.display = 'none';
            this.innerHTML = 'Read More';
            this.classList.remove('clicked');
        }
    });
});
