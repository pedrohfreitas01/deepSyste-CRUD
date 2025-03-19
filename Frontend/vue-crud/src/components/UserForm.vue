<template>
  <Dialog :visible.sync="visible" header="User Form">
    <InputText v-model="user.username" placeholder="Username" />
    <Dropdown v-model="user.roles" :options="roles" optionLabel="label" placeholder="Roles" />
    <InputText v-model="user.timezone" placeholder="Timezone" />
    <Checkbox v-model="user.isActive" label="Is Active?" />
    <Button label="Save" @click="saveUser" />
  </Dialog>
</template>

<script>
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import Checkbox from 'primevue/checkbox';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';

export default {
  components: {
    InputText,
    Dropdown,
    Checkbox,
    Button,
    Dialog
  },
  props: ['visible', 'user'],
  emits: ['save'],
  data() {
    return {
      roles: [{ label: 'Admin' }, { label: 'User' }]
    };
  },
  methods: {
    saveUser() {
      this.$emit('save', this.user);
    }
  }
};
</script>