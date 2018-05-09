<template>
  <div :class="cardSize">
    <div class="card">
      <div class="card-content">
        <div class="content">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'gongos-card',
  props: ['cardTitle', 'cardSize'],
  data () {
    return {

    }
  }
}
</script>
