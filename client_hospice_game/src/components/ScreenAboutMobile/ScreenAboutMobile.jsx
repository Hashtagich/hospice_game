import styles from './screenAboutMobile.module.css';
import Button from '../Button/Button';
import imagePhone from '../../images/phone.png';
import imagePhoneMobile from '../../images/phoneForMobile.png'



const ScreenAboutMobile = () => {
    return (
        <section id='mobilegame' className={styles.container}>
            <img src={imagePhone} className={styles.image} alt="Foto mobile phone"></img>
            <div className={styles.wrapperDescriptionMobileVersion}>
                <h1 className={styles.sectionName}>Мобильная версия</h1>
                <p className={styles.description}>Можно играть и на мобильном устройстве</p>
                <img src={imagePhoneMobile} className={styles.imageMobile} alt="Foto mobile phone"></img>
                <a className={styles.bottomLine} href='https://www.figma.com/proto/wn8i34WXIVj03MoE4tyyBZ/%D0%97%D0%B0%D0%BC%D0%BE%D0%BA-%D0%B7%D0%B0%D0%B1%D0%BE%D1%82%D1%8B?node-id=1-320&node-type=canvas&t=SVYDaCDFBlwDrAO4-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A320' rel="noopener noreferrer" target='_blank'><Button className={styles.button} nameButton='Перейти'/></a>
                <Button className={styles.buttondisable} nameButton='Перейти'/>
                <h3 className={styles.infoDisabledButton}>Доступно на мобильном</h3>
            </div>
        </section>
    )
};

export default ScreenAboutMobile;