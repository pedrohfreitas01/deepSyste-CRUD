<template>
  <div>
    <Button label="Create User" @click="openCreateModal" />
    <DataTable :value="users">
      <Column field="username" header="Username">
        <template #body="{ data }">
          <router-link :to="`/user/${data.id}`">
            {{ data.username }}
          </router-link>
        </template>
      </Column>
      <Column field="roles" header="Roles" />
      <Column field="preferences.timezone" header="Timezone">
        <template #body="{ data }">
          {{ data.preferences?.timezone || "N/A" }}
        </template>
      </Column>
      <Column field="active" header="Is Active?">
        <template #body="{ data }">
          {{ data.active ? "Yes" : "No" }}
        </template>
      </Column>
      <Column field="lastUpdatedAt" header="Last Updated At" />
      <Column field="createdAt" header="Created At" />
      <Column header="Actions">
        <template #body="{ data }">
          <Button icon="pi pi-pencil" @click="openEditModal(data)" />
          <Button icon="pi pi-trash" @click="openDeleteDialog(data.id)" />
        </template>
      </Column>
    </DataTable>

    <UserForm
      v-model:visible="isModalVisible"
      :user="selectedUser"
      @save="saveUser"
    />

    <ConfirmDialog
      v-model:visible="isDeleteDialogVisible"
      message="Are you sure?"
      @confirm="deleteUser"
      @cancel="isDeleteDialogVisible = false"
    />
  </div>
</template>

<script>
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import UserForm from "../components/UserForm.vue";
import ConfirmDialog from "../components/ConfirmDialog.vue";
import userService from "../services/userService";

export default {
  components: {
    Button,
    DataTable,
    Column,
    UserForm,
    ConfirmDialog,
  },
  data() {
    return {
      users: [],
      isModalVisible: false,
      isDeleteDialogVisible: false,
      selectedUser: {},
      userIdToDelete: null,
    };
  },
  created() {
    this.loadUsers();
  },
  methods: {
    async loadUser() {
      const userId = this.$route.params.id;
      if (!userId) {
        console.error("User ID not found.");
        return;
      }

      try {
        this.user = await userService.getUser(userId);
      } catch (error) {
        console.error("Error loading user:", error);
      }
    },
    openCreateModal() {
      this.selectedUser = {};
      this.isModalVisible = true;
    },
    openEditModal(user) {
      this.selectedUser = { ...user };
      this.isModalVisible = true;
    },
    openDeleteDialog(id) {
      this.userIdToDelete = id;
      this.isDeleteDialogVisible = true;
    },
    async saveUser(user) {
      try {
        if (user.username && user.username.trim() !== "") {
          await userService.updateUser(user.username, user);
        } else {
          await userService.createUser(user);
        }
        await this.loadUsers();
        this.isModalVisible = false;
      } catch (error) {
        console.error("Error saving user:", error);
      }
    },
    async deleteUser() {
      if (!this.userIdToDelete) {
        console.error("Error: No user to delete.");
        return;
      }

      try {
        await userService.deleteUser(this.userIdToDelete);
        await this.loadUsers();
        this.isDeleteDialogVisible = false;
      } catch (error) {
        console.error("Error deleting user:", error);
      }
    },
  },
};
</script>
