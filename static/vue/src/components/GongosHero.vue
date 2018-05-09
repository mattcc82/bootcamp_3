<template>
  <section class="hero is-bold is-danger is-radiusless" :class="heroClass">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column is-8-desktop is-offset-2-desktop">
            <h1 class="title is-2 is-spaced">
              {{ title }}
            </h1>
            <h2 class="subtitle is-4">
              {{ subtitle }}
            </h2>
          </div>
          <div class="column">
            <button 
              type="button" 
              @click="getData()" 
              class="button is-danger is-inverted is-outlined is-large" 
              :class="{ 'is-loading': isLoading, 'focused': isLoading }">
              See Results
              <i class="fas fa-angle-right" style="width: 2rem;"></i>
            </button>
            <br>
            <br>
            <progress v-show="isLoading" class="progress is-small" :value="loadCompleted" max="100">{{ loadCompleted }}</progress>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { EventBus } from '../app'
export default {
  name: 'gongos-hero',
  props: [
    'title', 'subtitle', 'isLoading', 'heroClass', 'loadCompleted'
  ],
  data () {
    return {
    }
  },
  methods: {
    getData: function () {
      EventBus.$emit('getData', 0)
    }
  }
}
</script>
