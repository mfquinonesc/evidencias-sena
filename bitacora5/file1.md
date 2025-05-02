## Modificación de Componentes Rutas

Esta modificación se realizó para poder incluir el título de cada componente en el encabezado, pasando el título del componente hijo al componente padre. También se creó un arreglo con el componente y la ruta correspondiente.

### Modificado

  ```jsx
  // This array contains the components and tokens of the stylesheet section
  // Every component must have a setSubtitle method which set the subtitle in the parent component
  // Every component can use the hook isWideAspect to get the parent aspect ration
  const stylesheetComponents = [
    { path: "logos", component: Logos },
    { path: "tipografias", component: Texts },
    { path: "colores", component: Colors },
    { path: "filetes", component: Filetes },
    { path: "iconografia", component: Iconography },
    { path: "grillas", component: Grids },
    { path: "aspect ratio", component: AspectRatio },
    { path: "efectos", component: Effects },
    { path: "botones", component: Buttons },
    { path: "notificaciones", component: Notifications },
    { path: "hover", component: Hover },
    { path: "cards", component: Cards },
    { path: "paginadores", component: Pager },
    { path: "scrolls", component: Scrolls },
    { path: "tablas fijas", component: FixedTales },
    { path: "tablas paginadas", component: PaginatedTables },
    { path: "barra de texto animado", component: AnimatedTextBar },
    { path: "modales", component: Modals },
    { path: "calendarios", component: Calendar },
    { path: "navbars", component: Navbars },
    { path: "sliders", component: Sliders },
    { path: "progressbar", component: Progressbar },
    { path: "tooltip", component: ToolTip },
  ]; 
 ```

 ```jsx
   <Route path="/stylesheet" element={<Stylesheet subtitle={subtitle} />} >
        {stylesheetComponents.map((comp, indx) => {
            return (
                <Route
                key={indx}
                path={comp.path}
                element={<comp.component setSubtitle={setSubtitle} />}
                />
            );
        })}
    </Route>
 ```

### Anterior

```jsx
<Route path="/stylesheet" element={<Stylesheet />}>
  <Route path="logos" element={<Logos />} />
  <Route path="tipografias" element={<Texts />} />
  <Route path="colores" element={<Colors />} />
  <Route path="filetes" element={<Filetes />} />
  <Route path="iconografia" element={<Iconography />} />
  <Route path="grillas" element={<Grids />} />
  <Route path="aspect ratio" element={<AspectRatio />} />
  <Route path="efectos" element={<Effects />} />
  <Route path="botones" element={<Buttons />} />
  <Route path="notificaciones" element={<Notifications />} />
  <Route path="hover" element={<Hover />} />
  <Route path="cards" element={<Cards />} />
  <Route path="paginadores" element={<Pager />} />
  <Route path="scrolls" element={<Scrolls />} />
  <Route path="tablas fijas" element={<FixedTales />} />
  <Route path="tablas paginadas" element={<PaginatedTables />} />
  <Route path="barra de texto animado" element={<AnimatedTextBar />} />
  <Route path="modales" element={<Modals />} />
  <Route path="calendarios" element={<Calendar />} />
  <Route path="navbars" element={<Navbars />} />
  <Route path="sliders" element={<Sliders />} />
  <Route path="progressbar" element={<Progressbar />} />
  <Route path="tooltip" element={<ToolTip />} />
</Route>
```