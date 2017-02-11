$(function() {
  const cssClasses = [
    'rangeslider--is-lowest-value',
    'rangeslider--is-highest-value'
  ];
  
  $('input[type=range]')
    .rangeslider({
      polyfill: false
    })
    .on('input', function() {
      const fraction = (this.value - this.min) / (this.max - this.min);
      if (fraction === 0) {
        this.nextSibling.classList.add(cssClasses[0]);
      } else if (fraction === 1) {
        this.nextSibling.classList.add(cssClasses[1]);
      } else {
        this.nextSibling.classList.remove(...cssClasses)
      }
    });
});