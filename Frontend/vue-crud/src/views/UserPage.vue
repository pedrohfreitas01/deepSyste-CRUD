<template>
  <div>
    <h1>{{ user.username }}</h1>
    <p>Roles: {{ user.roles }}</p>
    <p>Timezone: {{ user.preferences?.timezone }}</p>
    <p>Is Active?: {{ user.active ? "Yes" : "No" }}</p>
    <p>Last Updated At: {{ user.lastUpdatedAt }}</p>
    <p>Created At: {{ formatDate(user.created_ts) }}</p>
    <Button label="Edit" @click="openEditModal" />
    <Button label="Delete" @click="openDeleteDialog" />
    <UserForm :visible.sync="isModalVisible" :user="user" @save="saveUser" />
    <ConfirmDialog :visible.sync="isDeleteDialogVisible" message="Are you sure?" @confirm="deleteUser" @cancel="isDeleteDialogVisible = false" />
  </div>
</template>

<script>
import UserForm from '../components/UserForm.vue';
import ConfirmDialog from '../components/ConfirmDialog.vue';
import userService from '../services/userService';

export default {
  components: { UserForm, ConfirmDialog },
  data() {
    return {
      user: {},
      isModalVisible: false,
      isDeleteDialogVisible: false
    };
  },
  created() {
    this.loadUser();
  },
  methods: {
    async loadUser() {
      try {
        this.user = await userService.getUser(this.$route.params.id); 
      } catch (error) {
        console.error("Error loading user:", error);
      }
    },
    openEditModal() {
      this.isModalVisible = true;
    },
    openDeleteDialog() {
      this.isDeleteDialogVisible = true;
    },
    async saveUser(user) {
      try {
        await userService.updateUser(user.id, user); 
        this.loadUser();  
        this.isModalVisible = false;
      } catch (error) {
        console.error("Error saving user:", error);
      }
    },
    async deleteUser() {
      try {
        await userService.deleteUser(this.user.id); 
        this.$router.push('/');  
      } catch (error) {
        console.error("Error deleting user:", error);
      }
    },
    formatDate(timestamp) {
      const date = new Date(timestamp * 1000);
      return date.toLocaleString();
    }
  }
};
</script>
