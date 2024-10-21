import ScreenMain from '../src/components/ScreenMain/ScreenMain';
import ScreenAboutGame from '../src/components/ScreenAboutGame/ScreenAboutGame';
import ScreenAboutRealCenter from '../src/components/ScreenAboutRealCenter/ScreenAboutRealCenter';
import ScreenAboutGameplay from '../src/components/ScreenAboutGameplay/ScreenAboutGameplay';
import ScreenAboutMobile from '../src/components/ScreenAboutMobile/ScreenAboutMobile';
import TheHeader from './components/TheHeader/TheHeader';
import TheFooter from './components/TheFooter/TheFooter';
import ScreenFeatureGame from './components/ScreenFeatureGame/ScreenFeatureGame';
import styles from './app.module.css';
import { useEffect, useState } from 'react';


function App() {

const [headerColor, setHeaderColor] = useState(false)

useEffect(() => {
	window.addEventListener('scroll', function () {
		const scrollPos = window.scrollY;

		if(scrollPos > 640) {
			setHeaderColor(true);
		}else {
			setHeaderColor(false);
		}
	})
}, [])

	return (
		<>
			<TheHeader headerColor={headerColor}/>
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
