<template>
  <Dialog :visible.sync="visible" header="Confirm" :modal="true">
    <p>{{ message }}</p>
    <Button label="Yes" @click="confirm" />
    <Button label="No" @click="cancel" />
  </Dialog>
</template>

<script>
export default {
  props: ['visible', 'message'],
  emits: ['confirm', 'cancel'],
  methods: {
    confirm() {
      this.$emit('confirm');
    },
    cancel() {
      this.$emit('cancel');
    }
  }
};
</script>