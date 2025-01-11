import React, { useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";
import UserEditModal from "../components/UserEditModal"; // Asegúrate de importar el modal

const UsersPage = () => {
    const { user, users, getUsers, isAuthenticated, editUser, deactivateUser, activateUser } = useAuth();
    const [selectedUser, setSelectedUser] = useState(null);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        if (isAuthenticated && user?.role === "admin") {
            getUsers(); // Llama a getUsers solo si el usuario está autenticado y es admin
        }
    }, [isAuthenticated, user]);

    if (user?.role !== "admin") {
        return <Navigate to="/unauthorized" replace />;
    }

    const handleEdit = (u) => {
        setSelectedUser(u);
        setShowModal(true);
    };

    const handleSave = (updatedData) => {
        if (selectedUser?.id) {
            editUser(selectedUser.id, updatedData); // Llama a editUser con los datos actualizados
            setShowModal(false);
        }
    };

    const handleDeactivate = (id) => {
        if (!id) {
            console.error("El ID del usuario es undefined");
            return;
        }
        deactivateUser(id);
    };

    const handleActivate = (id) => {
        if (!id) {
            console.error("El ID del usuario es undefined");
            return;
        }
        activateUser(id);
    };

    return (
        <div>
            <h1>Lista de Usuarios</h1>
            {users.length > 0 ? (
                <table>
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Email</th>
                            <th>Teléfono</th>
                            <th>Género</th>
                            <th>Rol</th>
                            <th>Estado</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {users.map((u) => (
                            <tr key={u.id}>
                                <td>{u.first_name}</td>
                                <td>{u.last_name}</td>
                                <td>{u.email}</td>
                                <td>{u.phone}</td>
                                <td>{u.gender}</td>
                                <td>{u.role}</td>
                                <td>{u.is_active ? "Activo" : "Inactivo"}</td>
                                <td>
                                    <button onClick={() => handleEdit(u)}>
                                        Editar
                                    </button>
                                    {u.is_active ? (
                                        <button onClick={() => handleDeactivate(u.id)}>Desactivar</button>
                                    ) : (
                                        <button onClick={() => handleActivate(u.id)}>Activar</button>
                                    )}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>No se encontraron usuarios.</p>
            )}
            <UserEditModal
                showModal={showModal}
                onClose={() => setShowModal(false)}
                onSave={handleSave}
                user={selectedUser}
            />
        </div>
    );
};

export default UsersPage;