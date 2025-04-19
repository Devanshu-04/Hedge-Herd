const track = document.getElementById("image-track");

let isDragging = false;
let startX = 0;
let startY = 0;
const dragThreshold = 5; // Pixels threshold to differentiate between click and drag

const handleOnDown = e => {
  track.dataset.mouseDownAt = e.clientX;
  startX = e.clientX;
  startY = e.clientY;
  isDragging = false;
};

const handleOnUp = e => {
  track.dataset.mouseDownAt = "0";
  track.dataset.prevPercentage = track.dataset.percentage;

  // Check if it's a click (not a drag)
  if (!isDragging) {
    const clickedElement = document.elementFromPoint(e.clientX, e.clientY);
    if (clickedElement && clickedElement.tagName === "A") {
      clickedElement.click(); // Trigger the link click
    }
  }
};

const handleOnMove = e => {
  if (track.dataset.mouseDownAt === "0") return;

  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX;
  const maxDelta = window.innerWidth / 2;

  const percentage = (mouseDelta / maxDelta) * -100;
  const nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage;
  const nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);

  track.dataset.percentage = nextPercentage;

  track.animate({
    transform: `translate(${nextPercentage}%, -50%)`
  }, { duration: 1200, fill: "forwards" });

  for (const image of track.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${100 + nextPercentage}% center`
    }, { duration: 1200, fill: "forwards" });
  }

    // Optionally, animate the titles
  for (const title of track.getElementsByClassName("title")) {
    title.animate({
      opacity: 1, /* Fade in titles */
      transform: `translateX(${nextPercentage}%)` /* Slide titles */
    }, { duration: 1200, fill: "forwards" });
  }


  // Check if the movement exceeds the threshold to consider it a drag
  const deltaX = Math.abs(e.clientX - startX);
  const deltaY = Math.abs(e.clientY - startY);
  if (deltaX > dragThreshold || deltaY > dragThreshold) {
    isDragging = true;
  }
};

/* -- Event Listeners -- */

window.onmousedown = e => handleOnDown(e);
window.ontouchstart = e => handleOnDown(e.touches[0]);

window.onmouseup = e => handleOnUp(e);
window.ontouchend = e => handleOnUp(e.touches[0]);

window.onmousemove = e => handleOnMove(e);
window.ontouchmove = e => handleOnMove(e.touches[0]);


// Onboarding message when page first loads
document.addEventListener("DOMContentLoaded", () => {
  const onboardingMessage = document.getElementById("onboardingMessage");
  const slider = document.getElementById("imageSlider");

  onboardingMessage.classList.add("show");

  const hideOnboardingMessage = () => onboardingMessage.classList.remove("show");

  slider.addEventListener("mousedown", hideOnboardingMessage);
  slider.addEventListener("touchstart", hideOnboardingMessage);

  setTimeout(hideOnboardingMessage, 2000);
});
