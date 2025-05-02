## Modificación de las medias queries

Se agregaro las clases ```.stylesheet_mobil``` y ```.stylesheet_screen``` para ajustar el subtítulo según el aspect ratio. El subtítulo se ubica a la derecha en celulares y en tabletas y pantallas grandes se ubica a la izquierda.

Se utilizaron las siguientes definiciones de media queries para los distintos aspect ratios dados.

- ```@media (max-aspect-ratio: 3/4)```
- ```@media (min-aspect-ratio: 4/5) and (max-width: 1290px), (min-aspect-ratio: 3/2) and (max-width: 1290px)```
- ```@media (min-aspect-ratio: 16/9) and (max-width: 1290px)```

```css
.viewport_stylesheet {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(17, 1fr);
  height: 100vh;
  scroll-snap-align: start;
  position: relative;
}

.stylesheet_bg {
  position: absolute;
  background-color: #ffffff;
  z-index: -1;
  top: 12%;
  left: 5%;
  right: 5%;
  bottom: 6%;
  border-radius: 10px;
  box-shadow: 0px 0px 50px rgba(0, 0, 0, 0.15);
}

.stylesheet_header {
  grid-column: 2/12;
  grid-row: 5/7;
}

.stylesheet_header h1 {
  color: #eb162c;
  font-family: Bahnschrift;
  font-size: clamp(4rem, 6vw, 10rem);
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  text-transform: uppercase;
  margin: 0;
}

.stylesheet_section {
  grid-column: 2/9;
  grid-row: 7/9;
  column-gap: 2%;
}

.stylesheet_section h1 {
  color: #eb162c;
  font-family: Bahnschrift;
  font-size: clamp(4rem, 6vw, 10rem);
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  text-transform: uppercase;
  margin: 0;
}

.stylesheet_section img {
  padding: 0.5%;
}

.styelesheet_text {
  grid-column: 2/5;
  grid-row: 10/12;
}

.styelesheet_text-text {
  color: #000;
  text-align: justify;
  font-family: Bahnschrift;
  font-size: clamp(0.5rem, 3vw, 0.8rem);
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.styelesheet_heroImg {
  grid-column: 7/12;
  grid-row: 5/16;
}

.styelesheet_heroImg img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.stylesheet_title {
  grid-column: 4/10;
  grid-row: 3/5;
  color: #eb162c;
  text-align: center;
  font-family: Bahnschrift;
  font-size: clamp(1rem, 10vw, 2rem);
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  text-transform: uppercase;
  -webkit-tap-highlight-color: transparent;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.stylesheet_titles {
  grid-column: 2/4;
  grid-row: 6/8;
  color: var(--R1-color);
  font-family: Klik;
  font-size: clamp(1rem, 2vw, 1rem);
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  text-transform: uppercase;
  height: 50px;
  margin: 0;
  -webkit-tap-highlight-color: transparent;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.stylesheet_text {
  grid-column: 2/4;
  grid-row: 4/6;
  color: #000;
  font-family: Bahnschrift;
  font-size: clamp(0.1rem, 0.6vw, 0.7rem);
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  -webkit-tap-highlight-color: transparent;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.stylesheet_section svg {
  height: 5vw;
  width: fit-content;
}

.stylesheet_container-head-body {
  grid-column: 2/12;
  grid-row: 3/17;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;  
}

.stylesheet_container-head-body .stylesheet_mobil {
  display: none;
}

.stylesheet_container-head-body .stylesheet_screen {
  display: inline;
}

.stylesheet_container-head-body .stylesheet_head {
  width: 100%;
  height: 21.4285714286%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}

.stylesheet_container-head-body .stylesheet_head .stylesheet_head-bottom {
  width: 100%;
  height: calc(66.6666666667% - 1rem);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.stylesheet_container-head-body .stylesheet_head .stylesheet_head-titles {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  width: fit-content;
}

.stylesheet_container-head-body .stylesheet_body {
  width: 100%;
  height: 78.5714285714%;
}

.stylesheet_h1 {
  color: #eb162c;
  font-size: 4.1666666667vh;
  font-weight: 600;
  text-transform: uppercase;
  font-family: Bahnschrift;
  margin: 0;
  width: auto;
}

.stylesheet_h2 {
  color: #eb162c;
  font-size: 2.7777777778vh;
  font-weight: 500;
  text-transform: uppercase;
  font-family: Bahnschrift;
  margin: 0;
  width: auto;
}

.stylesheet_texts,
.styelesheet_text-text {
  font-size: 1.6666666667vh;
  font-family: Bahnschrift;
  margin: 0;
}

@media (max-aspect-ratio: 3/4) {
  .viewport_stylesheet {
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: repeat(34, 1fr);
  }

  .stylesheet_bg {
    top: 12%;
    left: 8%;
    right: 8%;
    bottom: 6%;
  }

  .stylesheet_title {
    grid-column: 2/12;
    grid-row: 6/8;
    text-align: center;
    font-size: clamp(1rem, 4vw, 3rem);
    margin: 0 auto;
  }

  .stylesheet_header {
    grid-column: 3/11;
    grid-row: 8/10;
    display: flex;
    justify-content: center;
  }

  .stylesheet_header h1 {
    font-size: clamp(2.5rem, 5vw, 7rem);
    text-wrap: nowrap;
  }

  .stylesheet_section {
    grid-column: 3/11;
    grid-row: 9/11;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding-left: calc(50% - 3rem);
    gap: 3vh;
  }

  .stylesheet_section svg {
    height: 2.5rem;
  }

  .stylesheet_logo {
    max-width: 10vh;
    max-height: 5vh;
  }

  .stylesheet_titles {
    grid-column: 7/11;
    grid-row: 7/9;
    font-size: clamp(0.7rem, 1vw, 1rem);
    margin-right: 2vh;
    display: flex;
    justify-content: end;
  }

  .stylesheet_text {
    grid-column: 3/11;
    grid-row: 9/11;
    font-size: clamp(0.4rem, 2vw, 1rem);
    text-align: center;
    align-self: start;
  }

  .styelesheet_text {
    grid-column: 3/11;
    grid-row: 25/28;
    text-align: center;
    align-self: start;
  }

  .styelesheet_text-text {
    font-size: clamp(0.6rem, 1vw, 1.5rem);
  }

  .styelesheet_heroImg {
    grid-column: 2/12;
    grid-row: 13/25;
  }

  .stylesheet_container-head-body {
    grid-row: 5/33;
  }

  .stylesheet_container-head-body .stylesheet_mobil {
    display: inline;
  }

  .stylesheet_container-head-body .stylesheet_screen {
    display: none;
  }

  .stylesheet_container-head-body .stylesheet_head {
    width: 100%;
    height: 28.5714285714%;
  }

  .stylesheet_container-head-body .stylesheet_head .stylesheet_head-bottom {
    justify-content: center;
    align-items: center;
  }

  .stylesheet_container-head-body .stylesheet_body {
    width: 100%;
    height: 71.4285714286%;
  }

  .stylesheet_h1 {
    font-size: 2.4264705882vh;
    text-align: center;
    width: 100%;
  }

  .stylesheet_h2 {
    font-size: 1.9117647059vh;
    text-align: end;
    width: 100%;
  }

  .stylesheet_texts,
  .styelesheet_text-text {
    font-size: 1.1470588235vh;
  }

  .stylesheet_texts-align {
    text-align: center;
  }

  .stylesheet_texts-width {
    max-width: 36.3970588235vh;
  }
}

@media (min-aspect-ratio: 4/5) and (max-width: 1290px), (min-aspect-ratio: 3/2) and (max-width: 1290px) {

  .stylesheet_container-head-body .stylesheet_mobil {
    display: inline;
  }

  .stylesheet_container-head-body .stylesheet_screen {
    display: none;
  }

  .stylesheet_container-head-body .stylesheet_head .stylesheet_head-bottom {
    height: calc(66.6666666667% - 2rem);
    justify-content: center;
  }

  .stylesheet_texts-align {
    text-align: center;
  }
}

@media (min-aspect-ratio: 16/9) and (max-width: 1290px) {
  
  .stylesheet_title {
    grid-row: 4/6;
    grid-column: 4/10;
    margin: 0 auto;
    text-align: center;
    font-size: 1.2rem;
  }

  .stylesheet_titles {
    grid-column: 5/9;
    grid-row: 5/7;
    font-size: clamp(0.7rem, 1vw, 1rem);
    padding-top: 1vh;
    padding-right: 2vh;
    padding: 0;
    display: flex;
    justify-content: end;
  }

  .stylesheet_text {
    grid-column: 4/11;
    grid-row: 6/8;
    font-size: clamp(0.1rem, 1.13vw, 0.7rem);
    margin: 0;
  }

  .stylesheet_header {
    grid-column: 2 / 10;
    grid-row: 5 / 8;   
    display: flex;;
    justify-content: flex-start;   
  }

  .stylesheet_header h1 {
    font-size: clamp(3rem, 5vw, 7rem);
  }

  .stylesheet_section {
    grid-column: 2/5;
    grid-row: 7/9;
    display: flex;
    justify-content: start;
    gap: 5vh;
    flex-direction: row;
  }

  .stylesheet_logo {
    max-width: 20vh;
    max-height: 12vh;
  }

  .styelesheet_text {
    grid-column: 2/7;
    grid-row: 10/13;
    text-align: center;
    align-self: start;
  }

  .styelesheet_text-text {
    font-size: clamp(0.6rem, 1vw, 1.5rem);
  }

  .stylesheet_container-head-body .stylesheet_mobil {
    display: inline;
  }

  .stylesheet_container-head-body .stylesheet_screen {
    display: none;
  }

  .stylesheet_container-head-body .stylesheet_head .stylesheet_head-bottom {
    height: calc(66.6666666667% - 1rem);
  }

  .stylesheet_texts,
  .styelesheet_text-text {
    font-size: 1.9117647059vh;
  }

  .stylesheet_texts-align {
    text-align: center;
  }
}
```

## Modificación del componente con el subtítulo 

### Modificado

```jsx
export default function Stylesheet({ subtitle = null }) {
  const location = useLocation();

  return (
    <StylesheetLayout>
      <div className="viewport_stylesheet"> 
        <div className="stylesheet_bg" />
        {location.pathname === "/stylesheet/" ||
        location.pathname === "/stylesheet" ? (
          <>
            <header className="stylesheet_header">
              <h1>
                Hoja de estilos <br />
                <span className="stylesheet_section">
                  para <LogoImg />
                </span>
              </h1>
            </header> 
            <section className="styelesheet_text">  
              <p className="styelesheet_text-text">
                El sistema de diseño y la hoja de estilos son los pilares para
                garantizar una identidad visual coherente y una experiencia de
                usuario consistente en el entorno telemático. Este enfoque
                define colores, tipografías, íconos y componentes reutilizables
                que representan la marca, asegurando que todas las plataformas
                (web, móvil o dispositivos integrados) reflejen profesionalismo,
                accesibilidad y funcionalidad. Una estructura visual sólida no
                solo unifica la percepción de la marca, sino que también
                facilita la escalabilidad y optimización en el dinámico mundo de
                los desarrollos de GPS Control.
              </p>
            </section>
            <section className="styelesheet_heroImg">
              <img src={HeroImg} alt="Hero" />
            </section>
          </>
        ) : (
          <>
            <div className="stylesheet_container-head-body">
              <div className="stylesheet_head">
                <div className="stylesheet_head-titles">
                  <h1 className="stylesheet_h1">HOJA DE ESTILOS GPS CONTROL</h1>
                  <h2 className="stylesheet_h2 stylesheet_mobil">
                    {subtitle != null ? subtitle : ""}
                  </h2>
                </div>

                <div className="stylesheet_head-bottom">
                  <p className="stylesheet_texts stylesheet_texts-align stylesheet_texts-width">
                    Galería de componentes y sus respectivos estilos para los
                    <br className="stylesheet_screen" />
                    montajes en los servicios web o websites
                  </p>

                  <h2 className="stylesheet_h2 stylesheet_screen">
                    {subtitle != null ? subtitle : ""}
                  </h2>
                </div>
              </div>
            </div>
            
            <Outlet />
          </>
        )}
      </div>
    </StylesheetLayout>
  );
}

```

### Anterior

```jsx
export default function Stylesheet() {
  const location = useLocation();

  return (
    <StylesheetLayout>
      <div className="viewport_stylesheet">
        <div className="stylesheet_bg" />
        {location.pathname === "/stylesheet/" ||
        location.pathname === "/stylesheet" ? (
          <>
            <header className="stylesheet_header">
              <h1>Hoja de estilos</h1>
            </header>
            <section className="stylesheet_section">
              <h1>para</h1>
              <LogoImg className="stylesheet_logo" />
            </section>
            <section className="styelesheet_text">
              <p className="styelesheet_text-text">
                El sistema de diseño y la hoja de estilos son los pilares para
                garantizar una identidad visual coherente y una experiencia de
                usuario consistente en el entorno telemático. Este enfoque
                define colores, tipografías, íconos y componentes reutilizables
                que representan la marca, asegurando que todas las plataformas
                (web, móvil o dispositivos integrados) reflejen profesionalismo,
                accesibilidad y funcionalidad. Una estructura visual sólida no
                solo unifica la percepción de la marca, sino que también
                facilita la escalabilidad y optimización en el dinámico mundo de
                los desarrollos de GPS Control.
              </p>
            </section>
            <section className="styelesheet_heroImg">
              <img src={HeroImg} alt="Hero" />
            </section>
          </>
        ) : (
          <>
            <h1 className="stylesheet_title">HOJA DE ESTILOS GPS CONTROL</h1>
            <p className="stylesheet_text">
              Galería de componentes y sus respectivos estilos para los montajes
              en los servicios web o websites
            </p>
            <Outlet />
          </>
        )}
      </div>
    </StylesheetLayout>
  );
}
```