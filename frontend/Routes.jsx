/* eslint-disable react/prop-types */
import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "./context/AuthContext";

export const ProtectedRoute = ({ role }) => {
    const { isAuthenticated, user, loading } = useAuth();

    // Si está cargando, puedes mostrar un mensaje
    if (loading) return <h1>Loading...</h1>;

    // Si no está autenticado, redirige al login
    if (!isAuthenticated) return <Navigate to="/login" replace />;

    // Si el rol no coincide, redirige a una página no autorizada
    if (role && user?.role !== role) return <Navigate to="/unauthorized" replace />;

    return <Outlet />;
};
