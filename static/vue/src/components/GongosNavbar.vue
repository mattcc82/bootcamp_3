<template>
  <nav class="navbar is-transparent is-fixed-top is-dark is-radiusless" role="navigation" aria-label="main navigation">
      <div class="navbar-brand is-lowercase">
        <a class="navbar-item is-fixed-top" :href="home">
          <span class="has-text-light"><i class="fab fa-bimobject"></i>ootcamp</span>
        </a>
        <div class="navbar-burger" data-target="navbarMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div class="navbar-menu" id="navbarMenu">
        <div class="navbar-start" style="border-left: 1px solid #fff;">
          <a class="navbar-item" :href="home">
            Home
          </a>
        </div>  
      </div>
    </nav>
</template>
<script>
import { BASE } from '../app'
export default {
  name: 'gongos-navbar',
  data () {
    return {
      home: BASE
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      // Get all "navbar-burger" elements
      var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0)
      // Check if there are any navbar burgers
      if ($navbarBurgers.length > 0) {
        // Add a click event on each of them
        $navbarBurgers.forEach(function ($el) {
          $el.addEventListener('click', function () {
            // Get the target from the "data-target" attribute
            var target = $el.dataset.target
            var $target = document.getElementById(target)
            // Toggle the class on both the "navbar-burger" and the "navbar-menu"
            $el.classList.toggle('is-active')
            $target.classList.toggle('is-active')
          })
        })
      }
    })
  }
}
</script>
