const buttons = document.querySelectorAll(".more-button");
const blocks = document.getElementsByClassName('more-block')

buttons.forEach(button => {
    button.addEventListener('click', function() {
        var active_blocks = document.querySelectorAll('.more-block_enabled');
        active_blocks.forEach(block => {
            if (block != this.parentElement) {
                block.classList.remove('more-block_enabled')
            }
        });
        
        this.parentElement.classList.toggle("more-block_enabled");
    });
});