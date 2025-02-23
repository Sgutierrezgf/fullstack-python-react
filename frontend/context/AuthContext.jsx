/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import { createContext, useContext, useState, useEffect } from "react";
import {
    registerRequest,
    loginRequest,
    getUsers as fetchUsers,
    editUser as updateUser,
} from "../api/auth";
import axios from "axios";




export const AuthContext = createContext();

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider");
    }

    return context;
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(() => {
        const storedUser = localStorage.getItem("user");
        return storedUser ? JSON.parse(storedUser) : null;
    });
    const [isAuthenticated, setIsAuthenticated] = useState(() => {
        const token = localStorage.getItem("access_token");
        return token ? true : false;
    });
    const [users, setUsers] = useState([]);
    const [errors, setErrors] = useState([]);

    // Sincronizar el usuario y el estado de autenticación en el localStorage
    useEffect(() => {
        if (user) {
            localStorage.setItem("user", JSON.stringify(user));
        } else {
            localStorage.removeItem("user");
        }
    }, [user]);

    useEffect(() => {
        if (isAuthenticated) {
            const token = localStorage.getItem("access_token");
            if (!token) {
                setIsAuthenticated(false);
                setUser(null);
            }
        } else {
            localStorage.removeItem("access_token");
        }
    }, [isAuthenticated]);

    const signup = async (user) => {
        try {
            const res = await registerRequest(user);
            console.log("Usuario creado:", res.data);
            // Redirigir al login después de registrarse exitosamente
        } catch (error) {
            setErrors(error.response.data);
        }
    };



    const signin = async (credentials) => {
        try {
            const res = await loginRequest(credentials);

            const { access, refresh, user } = res.data;

            localStorage.setItem("access_token", access);
            localStorage.setItem("refresh_token", refresh);

            setUser(user);
            setIsAuthenticated(true);
        } catch (error) {
            setErrors(error.response ? error.response.data : { detail: "Error inesperado" });
        }
    };
    const getUsers = async () => {
        try {
            const token = localStorage.getItem("access_token");
            if (!token) {
                throw new Error("No se encontró el token de acceso.");
            }
            console.log(token);

            const res = await fetchUsers({
                headers: { Authorization: `Bearer ${token}` },
            });
            setUsers(res.data);
        } catch (error) {
            console.error("Error al obtener usuarios:", error.response?.data || error.message);
            setErrors(error.response?.data || error.message);
        }
    };

    const editUser = async (id, userData) => {
        try {
            const token = localStorage.getItem("access_token");
            const res = await updateUser(id, userData, token);
            setUsers(users.map((u) => (u.id === id ? res.data : u))); // Actualizar el usuario en el estado
        } catch (error) {
            setErrors(error.response?.data || error.message);
        }
    };

    const activateUser = async (id) => {
        try {
            const token = localStorage.getItem("access_token");
            if (!token) {
                throw new Error("No se encontró el token de acceso.");
            }

            const res = await axios.put(
                `http://127.0.0.1:8000/api/users/activate/${id}/`,
                {},
                { headers: { Authorization: `Bearer ${token}` } }
            );

            // Actualiza la lista de usuarios después de la activación
            getUsers();
        } catch (error) {
            console.error("Error al activar usuario:", error.response?.data || error.message);
            setErrors(error.response?.data || error.message);
        }
    };

    const deactivateUser = async (id) => {
        try {
            const token = localStorage.getItem("access_token");
            if (!token) {
                throw new Error("No se encontró el token de acceso.");
            }

            const res = await axios.put(
                `http://127.0.0.1:8000/api/users/deactivate/${id}/`,
                {},
                { headers: { Authorization: `Bearer ${token}` } }
            );

            // Actualiza la lista de usuarios después de la desactivación
            getUsers();
        } catch (error) {
            console.error("Error al desactivar usuario:", error.response?.data || error.message);
            setErrors(error.response?.data || error.message);
        }
    };

    return (
        <AuthContext.Provider
            value={{
                user,
                users,
                isAuthenticated,
                errors,
                signin,
                signup,
                getUsers,
                editUser,
                deactivateUser,
                activateUser
            }}
        >
            {children}
        </AuthContext.Provider>
    );
};