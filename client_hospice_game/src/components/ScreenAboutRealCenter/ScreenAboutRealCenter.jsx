import styles from './screenAboutRealCenter.module.css';
import Button from '../Button/Button';


const ScreenAboutRealCenter = () => {
    return (
        <section className={styles.container}>
            <div className={styles.bigCircle}>
                <h1 className={styles.nameSection}>РЕАЛЬНЫЙ<br/>РЕАБИЛИТАЦИОННЫЙ<br/>ЦЕНТР</h1>
                <p className={styles.descriptionAboutMazaika}>«Мозайка» - реально существующий реабилитационный<br/> центр, который помогает детям и их семьям с разным<br/> состоянием здоровья.</p>
                <a href='https://detireb.ru/' target='_blank'><Button className={styles.button} nameButton='МОЗАЙКА'/></a>
            </div>
            <div className={styles.wrapperFotoGalery}>
                <div className={styles.wrapperFotoTop}>
                    <img className={styles.fotoTop}/>
                </div>
                <div className={styles.wrapperFotosBottom}>
                    <img className={styles.fotoLeft}/>
                    <img className={styles.fotoRight}/>
                </div>
            </div>
        </section>
    )
};

export default ScreenAboutRealCenter;