import styles from './screenAboutHero.module.css';


const ScreenAboutHero = () => {
    return (
        <section className={styles.container}>
            <div className={styles.wrapperFotoHeroes}>
                <img className={styles.fotoLeft}/>
                <img className={styles.fotoCenter}/>
                <img className={styles.fotoRight}/>
            </div>
            <div className={styles.wrapperDescriptionHeroes}>
                <h1 className={styles.sectionName}>ГЕРОИ</h1>
                <p className={styles.description}>Прототипами персонажей стали реальные работники центра,<br/> а истории посетителей вдохновили нас на создание персонажей<br/> главных героев.</p>
            </div>
        </section>
    )
};

export default ScreenAboutHero;