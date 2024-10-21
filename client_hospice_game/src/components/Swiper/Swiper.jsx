import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import { sliderData } from '../../datas/dataSlider';
import 'swiper/css/pagination';
import { Pagination } from 'swiper/modules';
import './styles.css';


const Swiperslider = () => {
    return (
        <Swiper
        initialSlide="1"
        slidesPerView={2}
        centeredSlides={true}
        spaceBetween={60}
        grabCursor={true}
        pagination={{
            clickable: true,
        }}
        modules={[Pagination]}
        className="mySwiper"
        >
            {sliderData.map((slide) => (
                <SwiperSlide key={slide.id}><img src={slide.image} alt='slides'></img></SwiperSlide>
            ))}
        </Swiper>
    )
};

export default Swiperslider;