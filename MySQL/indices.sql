CREATE UNIQUE INDEX idx_estudiantes_pregrado ON estudiapregrado(perCedulaEst);
CREATE UNIQUE INDEX idx_estudiantes_posgrados ON estudiaposgrado(perCedulaEst);
CREATE INDEX idx_estudiantes_solicitudes ON estudiante_has_solicitud(perCedulaEstudiante);
CREATE INDEX idx_facultades_solicitudes ON facultadsolicitud(solId);
CREATE INDEX idx_carrera_solicitud ON carrerasolicitud(solId);
CREATE INDEX idx_sede_solicitud ON sedesolicitud(solId);
CREATE INDEX idx_solicitud ON solicitud(solId);
CREATE INDEX idx_carrera ON carrera(carSNIES);