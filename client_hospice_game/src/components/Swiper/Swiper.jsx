import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import { sliderData } from '../../datas/dataSlider';
import styles from './swiper.module.css';
import 'swiper/css/pagination';
import { Pagination } from 'swiper/modules';
import './styles.css';


const Swiperslider = () => {
    return (
        <>
        <Swiper
        initialSlide="1"
        slidesPerView={2}
        centeredSlides={true}
        spaceBetween={60}
        grabCursor={true}
        pagination={{
            clickable: true,
            el: '.swiper-pagination',
            type: "bullets",
        }}
        modules={[Pagination]}
        className="mySwiper"
        >
            {sliderData.map((slide) => (
                <SwiperSlide key={slide.id}><img className={styles.positionImage} src={slide.image}></img></SwiperSlide>
            ))}
        </Swiper>
        <div class="swiper-pagination"></div>
        </>
    )
};

export default Swiperslider;