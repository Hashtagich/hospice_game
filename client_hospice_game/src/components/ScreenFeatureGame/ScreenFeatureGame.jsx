import styles from './screenFeatureGame.module.css';


const ScreenFeatureGame = () => {
    return (
        <section id='featuresgame' className={styles.container}>
            <h1 className={styles.title}>Особенности игры</h1>
            <div className={styles.wrapperFeatures}>
                <div className={styles.wrapperCell}>
                    <div className={styles.iconCellPurchase}></div>
                    <h2 className={styles.titleCell}>Покупка кабинетов</h2>
                    <h3 className={styles.subtitleCell}>Расширение возможностей реабилитационного центра</h3>
                </div>
                <div className={styles.wrapperCell}>
                <div className={styles.iconCellLevelup}></div>
                    <h2 className={styles.titleCell}>Улучшение уровня кабинетов</h2>
                    <h3 className={styles.subtitleCell}>Повышение качества услуг<br/> и оборудования</h3>
                </div>
                <div className={styles.wrapperCell}>
                <div className={styles.iconCellProcedure}></div>
                    <h2 className={styles.titleCell}>Отправка на процедуру</h2>
                    <h3 className={styles.subtitleCell}>Эффективное распределение<br/> ресурсов для каждой процедуры</h3>
                </div>
                <div className={styles.wrapperCell}>
                <div className={styles.iconCellIndividual}></div>
                    <h2 className={styles.titleCell}>Индивидуальные программы</h2>
                    <h3 className={styles.subtitleCell}>Настроенные под потребности<br/> каждого ребенка</h3>
                </div>
                <div className={styles.wrapperCell}>
                <div className={styles.iconCellMozikarehub}></div>
                    <h2 className={styles.titleCell}>Прототип центра «Мозаика»</h2>
                    <h3 className={styles.subtitleCell}>Помощь реальным детям  реабилитационного центра</h3>
                </div>
                <div className={styles.wrapperCell}>
                <div className={styles.iconCellFamily}></div>
                    <h2 className={styles.titleCell}>Семейное вовлечение</h2>
                    <h3 className={styles.subtitleCell}>Поддержка и советы для<br/> родителей и детей</h3>
                </div>
            </div>
        </section>
    )
};

export default ScreenFeatureGame;