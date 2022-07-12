"use strict"

document.addEventListener("DOMContentLoaded", function () {
  const rating = this;
  this.ratingValue = document.querySelectorAll(".items-top-left__rating-value");
  let numRating = 10.1;
  this.ratingValue.forEach(function (ratingValue) {

      numRating = numRating - 0.1
      ratingValue.innerHTML = numRating.toFixed(1);

  })
})