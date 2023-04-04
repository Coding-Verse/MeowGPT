const loading = document.getElementById('loading');
const form = document.querySelector('form');

form.addEventListener('submit', () => {
  loading.style.display = 'block';
});







var animationContainer = document.getElementById('loading');
var animationDataUrl = 'https://assets6.lottiefiles.com/packages/lf20_tr1pjkop.json';

var animData = {
  container: animationContainer,
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: animationDataUrl
};

var anim = bodymovin.loadAnimation(animData);




const textarea = document.querySelector('textarea');

textarea.addEventListener('input', function() {
  this.style.height = 'auto';
  this.style.height = this.scrollHeight + 'px';
});

var animateButton = function(e) {

  e.preventDefault;
  //reset animation
  e.target.classList.remove('animate');
  
  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  },700);
};




var animation = lottie.loadAnimation({
  container: document.getElementById('headpic'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'https://assets1.lottiefiles.com/packages/lf20_OT15QW.json'
});


var animation = lottie.loadAnimation({
  container: document.getElementById('meow-footer'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'https://assets9.lottiefiles.com/packages/lf20_jvtpl16e.json'
});


function scrollToBottom() {
  const scrollElement = document.scrollingElement || document.documentElement;
  scrollElement.scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });
}
