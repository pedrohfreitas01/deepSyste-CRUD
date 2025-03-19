import axios from "axios";

const API_URL = "http://localhost:5000/api/users";

export default {
  async getUsers() {
    try {
      const response = await axios.get(API_URL);
      return response.data;
    } catch (error) {
      console.error("Erro ao buscar usuários:", error);
      return [];
    }
  },

  async getUser(username) {
    try {
      const response = await axios.get(`${API_URL}/${username}`);
      return response.data;
    } catch (error) {
      console.error("Erro ao buscar usuário:", error);
      return {};
    }
  },

  async createUser(user) {
    try {
      await axios.post(API_URL, user);
    } catch (error) {
      console.error("Erro ao criar usuário:", error);
    }
  },

  async updateUser(username, user) {
    try {
      await axios.put(`${API_URL}/${username}`, user);
    } catch (error) {
      console.error("Erro ao atualizar usuário:", error);
    }
  },

  async deleteUser(username) {
    try {
      await axios.delete(`${API_URL}/${username}`);
    } catch (error) {
      console.error("Erro ao deletar usuário:", error);
    }
  },
};
