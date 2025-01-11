import axios from "./axios";

const API = "http://127.0.0.1:8000/api";


export const registerRequest = (user) =>
    axios.post(`${API}/register/`, user);
export const loginRequest = (user) =>
    axios.post(`${API}/login/`, user);
export const getUsers = () => axios.get(`${API}/users/`);
export const editUser = (id, userData, token) =>
    axios.put(`${API}/users/edit/${id}/`, userData, {
        headers: { Authorization: `Bearer ${token}` }
    });
export const deactivateUser = (id, token) =>
    axios.put(`${API}/users/deactivate/${id}/`, {}, {
        headers: { Authorization: `Bearer ${token}` }
    });
