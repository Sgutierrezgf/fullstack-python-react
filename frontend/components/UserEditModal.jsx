/* eslint-disable react/prop-types */
import { useState, useEffect } from 'react';
import './modal.css'

const UserEditModal = ({ showModal, user, onClose, onSave }) => {
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        gender: '',
        role: '',
    });

    useEffect(() => {
        if (user) {
            setFormData({
                first_name: user.first_name || '',
                last_name: user.last_name || '',
                email: user.email || '',
                phone: user.phone || '',
                gender: user.gender || '',
                role: user.role || '',
            });
        }
    }, [user]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(formData);
    };

    return (
        showModal && (
            <div className={`modal-overlay ${showModal ? 'show' : ''}`} onClick={onClose}>
                <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                    <button className="modal-close" onClick={onClose}>&times;</button>
                    <div className="modal-header">
                        <h2>Editar Usuario</h2>
                    </div>
                    <form onSubmit={handleSubmit}>
                        <div className="modal-body">
                            <input
                                type="text"
                                name="first_name"
                                value={formData.first_name}
                                onChange={handleChange}
                                placeholder="Primer nombre"
                            />
                            <input
                                type="text"
                                name="last_name"
                                value={formData.last_name}
                                onChange={handleChange}
                                placeholder="Apellido"
                            />
                            <input
                                type="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                placeholder="Email"
                            />
                            <input
                                type="text"
                                name="phone"
                                value={formData.phone}
                                onChange={handleChange}
                                placeholder="Teléfono"
                            />
                            <input
                                type="text"
                                name="gender"
                                value={formData.gender}
                                onChange={handleChange}
                                placeholder="Género"
                            />
                            <input
                                type="text"
                                name="role"
                                value={formData.role}
                                onChange={handleChange}
                                placeholder="Rol"
                            />
                        </div>
                        <div className="modal-footer">
                            <button type="submit">Guardar Cambios</button>
                        </div>
                    </form>
                </div>
            </div>
        )
    );
};

export default UserEditModal;
