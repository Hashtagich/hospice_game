import ScreenMain from '../src/components/ScreenMain/ScreenMain';
import ScreenAboutGame from '../src/components/ScreenAboutGame/ScreenAboutGame';
import ScreenAboutRealCenter from '../src/components/ScreenAboutRealCenter/ScreenAboutRealCenter';
import ScreenAboutGameplay from '../src/components/ScreenAboutGameplay/ScreenAboutGameplay';
import ScreenAboutMobile from '../src/components/ScreenAboutMobile/ScreenAboutMobile';
import TheHeader from './components/TheHeader/TheHeader';
import TheFooter from './components/TheFooter/TheFooter';
import ScreenFeatureGame from './components/ScreenFeatureGame/ScreenFeatureGame';
import styles from './app.module.css';


function App() {
	return (
		<>
			<TheHeader/>
			<main className={styles.main}>
				<ScreenMain/>
				<ScreenAboutGame/>
				<ScreenFeatureGame/>
				<ScreenAboutGameplay/>
				<ScreenAboutMobile/>
				<ScreenAboutRealCenter/>
			</main>
			<TheFooter/>
		</>
	);
}

export default App;
