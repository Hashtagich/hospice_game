import styles from './screenAboutGameplay.module.css';
import Swiper from '../Swiper/Swiper';
import SwiperMobile from '../SwiperMobile/SwiperMobile';


const ScreenAboutGameplay = () => {

    return (
        <section id='gameplay' className={styles.container}>
            <div className={styles.wrapperGeneral}>
                <h1 className={styles.sectionName}>Геймплей</h1>
                <div className={styles.wrapperSlider}>
                    <Swiper/>
                </div>
                <div className={styles.wrapperSliderMobile}>
                    <SwiperMobile/>
                </div>
            </div>
        </section>
    )
};

export default ScreenAboutGameplay;