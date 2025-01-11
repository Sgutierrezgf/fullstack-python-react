import { useForm } from "react-hook-form";
import { useAuth } from "../context/AuthContext";
import { Link, useNavigate } from "react-router-dom";
import { useEffect } from "react";
import '../src/index.css'

function LoginPage() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm();
    const { signin, isAuthenticated } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) navigate("/users");
    }, [isAuthenticated, navigate]);

    const onSubmit = handleSubmit((data) => {
        signin(data, navigate); // Pasamos 'navigate' para redirigir después de iniciar sesión
    });

    return (
        <div className="container">
            <h1>Inicio de sesión</h1>
            <form onSubmit={onSubmit}>
                <input
                    type="email"
                    {...register("email", { required: true })}
                    placeholder="example@example.com"
                />
                {errors.email && <p className="error">Email is required</p>}
                <input
                    type="password"
                    {...register("password", { required: true })}
                    placeholder="Password"
                />
                {errors.password && <p className="error">Password is required</p>}
                <button type="submit">Iniciar sesión</button>
                <p>
                    No tienes una cuenta?{" "}
                    <Link to="/register">Regístrate</Link>
                </p>
            </form>
        </div>
    );
}

export default LoginPage;