import { Suspense, lazy } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "../context/AuthContext";
import { ProtectedRoute } from "../Routes";


const LoginPage = lazy(() => import("../pages/Login"));
const UsersPage = lazy(() => import("../pages/Users"));
const RegisterPage = lazy(() => import("../pages/Register"));
const HomePage = lazy(() => import("../pages/Home"));



function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            {/* Rutas públicas */}
            <Route path="/" element={<HomePage />} />

            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />


            {/* Rutas protegidas */}
            <Route element={<ProtectedRoute role="admin" />}>
              <Route path="/users" element={<UsersPage />} />
            </Route>

            {/* Ruta para no autorizados */}
            <Route path="/unauthorized" element={<div>No tienes permiso para acceder a esta página.</div>} />
          </Routes>
        </Suspense>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;