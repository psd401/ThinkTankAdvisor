import chatgpt from "../assets/chatgpt.svg";
import youtubelogo from "../assets/youtubelogo.svg";
import psdlogo from "../assets/psd_logo-2color-fulllandscape.svg";


function Logo() {
    return (
        <div>
            <div id="logo">
                <img id="img-psdlogo" src={psdlogo}/>
            </div>
            <div id="logo-text">PSD AI</div>
        </div>
    )
}

export default Logo
