import styles from './screenAboutGameplay.module.css';
//import Slider from '../Slider/Slider';
import Swiper from '../Swiper/Swiper';


const ScreenAboutGameplay = () => {

    return (
        <section id='gameplay' className={styles.container}>
            <div className={styles.wrapperGeneral}>
                <h1 className={styles.sectionName}>Геймплей</h1>
                <div className={styles.wrapperSlider}>
                    <Swiper/>
                </div>
            </div>
        </section>
    )
};

export default ScreenAboutGameplay;