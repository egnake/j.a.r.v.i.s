<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVIS - AI Assistant</title>
    <meta name="theme-color" content="#000000">
    <link rel="manifest" href="data:application/json,{&quot;name&quot;:&quot;JARVIS AI Assistant&quot;,&quot;short_name&quot;:&quot;JARVIS&quot;,&quot;start_url&quot;:&quot;.&quot;,&quot;display&quot;:&quot;standalone&quot;,&quot;theme_color&quot;:&quot;#000000&quot;,&quot;background_color&quot;:&quot;#000000&quot;}">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-bg: #000000;
            --secondary-bg: #0a0a0a;
            --tertiary-bg: #1a1a1a;
            --quaternary-bg: #2a2a2a;
            --glass-bg: rgba(15, 15, 15, 0.85);
            --dark-glass: rgba(5, 5, 5, 0.9);
            --primary-text: #ffffff;
            --secondary-text: #a0a0a0;
            --tertiary-text: #707070;
            --accent-text: #00d4ff;
            --success-color: #00ff88;
            --warning-color: #ff9500;
            --error-color: #ff3366;
            --neon-blue: #0099ff;
            --neon-purple: #6644cc;
            --neon-pink: #ff4488;
            --neon-green: #00ff88;
            --neon-cyan: #00ffff;
            --border-dark: rgba(255, 255, 255, 0.05);
            --border-light: rgba(255, 255, 255, 0.1);
            --shadow-dark: rgba(0, 0, 0, 0.8);
            --shadow-neon: rgba(0, 153, 255, 0.3);
        }

        body {
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--primary-bg);
            color: var(--primary-text);
            min-height: 100vh;
            padding: 0;
            overflow-x: hidden;
            position: relative;
        }

        /* Ultra dark animated background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 15% 85%, rgba(0, 153, 255, 0.03) 0%, transparent 60%),
                radial-gradient(circle at 85% 15%, rgba(102, 68, 204, 0.03) 0%, transparent 60%),
                radial-gradient(circle at 50% 50%, rgba(255, 68, 136, 0.02) 0%, transparent 70%),
                linear-gradient(135deg, rgba(0, 0, 0, 0.95) 0%, rgba(10, 10, 10, 0.95) 100%);
            z-index: -1;
            animation: bgFloat 25s ease-in-out infinite;
        }

        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 98px,
                    rgba(0, 153, 255, 0.01) 100px
                ),
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 98px,
                    rgba(102, 68, 204, 0.01) 100px
                );
            z-index: -1;
            opacity: 0.3;
        }

        @keyframes bgFloat {
            0%, 100% { transform: translate(0, 0) rotate(0deg); opacity: 0.7; }
            25% { transform: translate(-15px, -10px) rotate(0.5deg); opacity: 0.9; }
            50% { transform: translate(10px, -15px) rotate(-0.5deg); opacity: 0.8; }
            75% { transform: translate(-10px, 10px) rotate(0.3deg); opacity: 0.9; }
        }

        .container {
            max-width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            position: relative;
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.9) 0%, rgba(10, 10, 10, 0.95) 100%);
        }

        .header {
            padding: 25px 20px;
            text-align: center;
            background: var(--dark-glass);
            backdrop-filter: blur(25px);
            border-bottom: 1px solid var(--border-dark);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px var(--shadow-dark);
        }

        .logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            margin-bottom: 12px;
        }

        .logo-icon {
            width: 55px;
            height: 55px;
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            animation: logoFloat 4s ease-in-out infinite;
            box-shadow: 
                0 0 20px rgba(0, 153, 255, 0.4),
                inset 0 0 20px rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(0, 153, 255, 0.3);
        }

        @keyframes logoFloat {
            0%, 100% { 
                transform: translateY(0px) rotate(0deg) scale(1); 
                box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);
            }
            50% { 
                transform: translateY(-8px) rotate(3deg) scale(1.05); 
                box-shadow: 0 0 30px rgba(0, 153, 255, 0.6);
            }
        }

        .logo {
            font-size: 2.4rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple), var(--neon-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 3px;
            text-shadow: 0 0 30px rgba(0, 153, 255, 0.5);
            animation: textGlow 3s ease-in-out infinite alternate;
        }

        @keyframes textGlow {
            from { filter: brightness(1) drop-shadow(0 0 5px rgba(0, 153, 255, 0.5)); }
            to { filter: brightness(1.2) drop-shadow(0 0 15px rgba(0, 153, 255, 0.8)); }
        }

        .subtitle {
            font-size: 0.85rem;
            color: var(--secondary-text);
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            opacity: 0.8;
        }

        .status-bar {
            padding: 18px 25px;
            margin: 15px 20px;
            border-radius: 25px;
            text-align: center;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-dark);
            background: var(--tertiary-bg);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        .status-bar.active {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.15), rgba(0, 153, 255, 0.15));
            border: 1px solid rgba(0, 255, 136, 0.3);
            box-shadow: 
                0 0 40px rgba(0, 255, 136, 0.3),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-green);
        }

        .status-bar.passive {
            background: linear-gradient(135deg, rgba(102, 68, 204, 0.15), rgba(255, 68, 136, 0.15));
            border: 1px solid rgba(102, 68, 204, 0.3);
            box-shadow: 
                0 0 40px rgba(102, 68, 204, 0.3),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-purple);
        }

        .status-bar.chat-mode {
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.15), rgba(0, 255, 255, 0.15));
            border: 1px solid rgba(0, 153, 255, 0.4);
            box-shadow: 
                0 0 40px rgba(0, 153, 255, 0.4),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-cyan);
        }

        .status-bar.code-mode {
            background: linear-gradient(135deg, rgba(255, 149, 0, 0.15), rgba(255, 68, 136, 0.15));
            border: 1px solid rgba(255, 149, 0, 0.4);
            box-shadow: 
                0 0 40px rgba(255, 149, 0, 0.4),
                0 8px 32px var(--shadow-dark);
            color: var(--warning-color);
        }

        .chat-container {
            flex: 1;
            padding: 25px;
            overflow-y: auto;
            max-height: calc(100vh - 350px);
            scroll-behavior: smooth;
            background: rgba(0, 0, 0, 0.2);
        }

        .message {
            margin-bottom: 25px;
            padding: 20px 25px;
            border-radius: 28px;
            max-width: 85%;
            word-wrap: break-word;
            animation: messageSlide 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(15px);
            border: 1px solid var(--border-dark);
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 32px var(--shadow-dark);
        }

        .message::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        }

        .message::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.03) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
        }

        .message:hover::after {
            opacity: 1;
        }

        @keyframes messageSlide {
            from { 
                opacity: 0; 
                transform: translateY(40px) scale(0.9); 
                filter: blur(5px);
            }
            to { 
                opacity: 1; 
                transform: translateY(0) scale(1); 
                filter: blur(0);
            }
        }

        .user-message {
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(102, 68, 204, 0.1));
            margin-left: auto;
            text-align: right;
            border-left: 3px solid var(--neon-blue);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(0, 153, 255, 0.2);
        }

        .jarvis-message {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.08), rgba(0, 153, 255, 0.08));
            margin-right: auto;
            border-left: 3px solid var(--neon-green);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(0, 255, 136, 0.2);
        }

        .system-message {
            background: linear-gradient(135deg, rgba(255, 149, 0, 0.08), rgba(255, 68, 136, 0.08));
            margin: 0 auto;
            text-align: center;
            font-style: italic;
            border-left: 3px solid var(--warning-color);
            max-width: 75%;
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(255, 149, 0, 0.2);
        }

        .input-section {
            background: var(--dark-glass);
            backdrop-filter: blur(25px);
            padding: 30px 25px;
            border-top: 1px solid var(--border-dark);
            position: sticky;
            bottom: 0;
            box-shadow: 0 -8px 32px var(--shadow-dark);
        }

        .server-config {
            margin-bottom: 25px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 20px;
            border: 1px solid var(--border-dark);
            backdrop-filter: blur(10px);
            box-shadow: 
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 4px 20px var(--shadow-dark);
        }

        .config-row {
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
            align-items: center;
        }

        .config-row:last-child {
            margin-bottom: 0;
        }

        .config-input {
            flex: 1;
            padding: 15px 20px;
            border: 1px solid var(--border-light);
            border-radius: 15px;
            background: rgba(0, 0, 0, 0.6);
            color: var(--primary-text);
            font-size: 14px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        .config-input:focus {
            outline: none;
            border-color: var(--neon-blue);
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 
                0 0 25px rgba(0, 153, 255, 0.3),
                inset 0 2px 10px rgba(0, 0, 0, 0.7);
            transform: translateY(-1px);
        }

        .config-input::placeholder {
            color: var(--tertiary-text);
        }

        .input-group {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            align-items: flex-end;
        }

        .message-input {
            flex: 1;
            padding: 18px 25px;
            border: 1px solid var(--border-light);
            border-radius: 28px;
            background: rgba(0, 0, 0, 0.6);
            color: var(--primary-text);
            font-size: 16px;
            backdrop-filter: blur(15px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            resize: none;
            min-height: 56px;
            max-height: 140px;
            box-shadow: 
                inset 0 2px 15px rgba(0, 0, 0, 0.6),
                0 4px 20px var(--shadow-dark);
        }

        .message-input:focus {
            outline: none;
            border-color: var(--neon-blue);
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 
                0 0 30px rgba(0, 153, 255, 0.4),
                inset 0 2px 15px rgba(0, 0, 0, 0.8);
            transform: translateY(-3px);
        }

        .message-input::placeholder {
            color: var(--tertiary-text);
        }

        .btn {
            padding: 18px 28px;
            border: none;
            border-radius: 22px;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-transform: uppercase;
            letter-spacing: 1.2px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(15px);
            border: 1px solid var(--border-light);
            box-shadow: 0 8px 32px var(--shadow-dark);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
            transition: left 0.6s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn:active {
            transform: scale(0.95);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--neon-blue), rgba(0, 153, 255, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(0, 153, 255, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(0, 153, 255, 0.5);
        }

        .btn-primary:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(0, 153, 255, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-secondary {
            background: linear-gradient(135deg, var(--neon-purple), rgba(102, 68, 204, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(102, 68, 204, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(102, 68, 204, 0.5);
        }

        .btn-secondary:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(102, 68, 204, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-success {
            background: linear-gradient(135deg, var(--neon-green), rgba(0, 255, 136, 0.7));
            color: var(--primary-bg);
            box-shadow: 
                0 0 25px rgba(0, 255, 136, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(0, 255, 136, 0.5);
        }

        .btn-success:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(0, 255, 136, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-danger {
            background: linear-gradient(135deg, var(--error-color), rgba(255, 51, 102, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(255, 51, 102, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(255, 51, 102, 0.5);
        }

        .btn-warning {
            background: linear-gradient(135deg, var(--warning-color), rgba(255, 149, 0, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(255, 149, 0, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(255, 149, 0, 0.5);
        }

        .controls {
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 15px;
            margin-bottom: 25px;
        }

        .mode-controls {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }

        .voice-btn {
            width: 65px;
            height: 65px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            position: relative;
        }

        .voice-btn.listening {
            animation: voicePulse 1.8s ease-in-out infinite;
        }

        @keyframes voicePulse {
            0% { 
                transform: scale(1); 
                box-shadow: 
                    0 0 25px rgba(255, 51, 102, 0.6),
                    0 0 0 0 rgba(255, 51, 102, 0.7); 
            }
            70% { 
                transform: scale(1.1); 
                box-shadow: 
                    0 0 35px rgba(255, 51, 102, 0.8),
                    0 0 0 25px rgba(255, 51, 102, 0); 
            }
            100% { 
                transform: scale(1); 
                box-shadow: 
                    0 0 25px rgba(255, 51, 102, 0.6),
                    0 0 0 0 rgba(255, 51, 102, 0); 
            }
        }

        .quick-commands {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
            gap: 15px;
        }

        .quick-btn {
            padding: 15px 20px;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--border-light);
            border-radius: 18px;
            color: var(--primary-text);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 13px;
            font-weight: 600;
            backdrop-filter: blur(15px);
            text-align: center;
            box-shadow: 
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 4px 20px var(--shadow-dark);
            position: relative;
            overflow: hidden;
        }

        .quick-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(102, 68, 204, 0.1));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .quick-btn:hover {
            background: rgba(0, 0, 0, 0.8);
            transform: translateY(-3px);
            box-shadow: 
                0 0 20px rgba(0, 153, 255, 0.3),
                0 8px 30px var(--shadow-dark);
            border-color: rgba(0, 153, 255, 0.4);
        }

        .quick-btn:hover::before {
            opacity: 1;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 25px;
            margin: 25px 0;
        }

        .loading-content {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            color: var(--neon-blue);
            font-weight: 600;
            font-size: 1.1rem;
        }

        .spinner {
            width: 28px;
            height: 28px;
            border: 4px solid rgba(0, 153, 255, 0.2);
            border-radius: 50%;
            border-top-color: var(--neon-blue);
            animation: spin 1.2s linear infinite;
            box-shadow: 0 0 15px rgba(0, 153, 255, 0.4);
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .connection-status {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
            margin-top: 12px;
            justify-content: center;
            font-weight: 600;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--error-color);
            animation: statusBlink 2.5s ease-in-out infinite;
            box-shadow: 0 0 10px var(--error-color);
        }

        .status-dot.connected {
            background: var(--neon-green);
            box-shadow: 0 0 15px var(--neon-green);
            animation: none;
        }

        @keyframes statusBlink {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.8); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .logo {
                font-size: 2rem;
            }
            
            .controls {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            
            .input-group {
                flex-direction: column;
                gap: 12px;
            }
            
            .config-row {
                flex-direction: column;
                align-items: stretch;
            }
            
            .voice-btn {
                width: 100%;
                height: 55px;
                border-radius: 28px;
            }

            .quick-commands {
                grid-template-columns: repeat(2, 1fr);
            }

            .chat-container {
                padding: 20px;
                max-height: calc(100vh - 380px);
            }
        }

        @media (max-width: 480px) {
            .header {
                padding: 20px 15px;
            }
            
            .chat-container {
                padding: 15px;
                max-height: calc(100vh - 400px);
            }
            
            .input-section {
                padding: 25px 15px;
            }
            
            .message {
                max-width: 95%;
                padding: 16px 20px;
            }

            .logo {
                font-size: 1.8rem;
            }

            .quick-commands {
                grid-template-columns: 1fr;
            }
        }

        /* Ultra dark scrollbar */
        .chat-container::-webkit-scrollbar {
            width: 8px;
        }

        .chat-container::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 4px;
        }

        .chat-container::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, rgba(0, 153, 255, 0.6), rgba(102, 68, 204, 0.6));
            border-radius: 4px;
            box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.8);
        }

        .chat-container::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, rgba(0, 153, 255, 0.8), rgba(102, 68, 204, 0.8));
            box-shadow: 0 0 10px rgba(0, 153, 255, 0.5);
        }

        /* Loading pulse effect */
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Advanced hover effects */
        .message:hover {
            transform: translateY(-2px);
            box-shadow: 
                0 12px 40px var(--shadow-dark),
                0 0 20px rgba(0, 153, 255, 0.2);
        }

        /* Notification styles */
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: rgba(0, 0, 0, 0.9);
            border: 1px solid var(--neon-green);
            border-radius: 12px;
            color: var(--neon-green);
            font-weight: 600;
            backdrop-filter: blur(15px);
            box-shadow: 0 8px 32px var(--shadow-dark);
            z-index: 1000;
            animation: slideInRight 0.5s ease;
        }

        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-container">
                <div class="logo-icon">🤖</div>
                <div>
                    <div class="logo">JARVIS</div>
                    <div class="subtitle">AI ASSISTANT</div>
                </div>
            </div>
        </div>

        <div class="status-bar passive" id="statusBar">
            <span id="statusText">🔴 Asistan Pasif - Bağlantı Bekleniyor</span>
        </div>

        <div class="chat-container" id="chatContainer">
            <div class="message system-message">
                <strong>🚀 JARVIS AI Assistant v2.0 - Ultra Dark Edition</strong><br>
                PC'nizdeki JARVIS Python koduna bağlanmak için aşağıdaki adımları takip edin:<br>
                <br>
                <strong>📋 Bağlantı Adımları:</strong><br>
                1️⃣ PC'nizde JARVIS Python kodunu çalıştırın<br>
                2️⃣ PC'nizin IP adresini öğrenin (cmd > ipconfig)<br>
                3️⃣ IP adresini aşağıya girin<br>
                4️⃣ "Test" butonuna basın<br>
                5️⃣ "Aktif Et" ile asistanı başlatın<br>
                <br>
                <small style="opacity: 0.7;">💡 Python kodunuz çalışırken mobil cihazınızdan tüm JARVIS özelliklerini kontrol edebilirsiniz.</small>
            </div>
        </div>

        <div class="input-section">
            <div class="server-config">
                <div class="config-row">
                    <input type="text" class="config-input" id="serverIP" placeholder="🌐 PC IP Adresi (örn: 192.168.1.100)" value="">
                    <input type="text" class="config-input" id="serverPort" placeholder="🔌 Port (Flask sunucu portu)" value="5000">
                </div>
                <div class="connection-status">
                    <div class="status-dot" id="connectionDot"></div>
                    <span id="connectionText">Bağlantı Bekleniyor</span>
                </div>
            </div>

            <div class="input-group">
                <textarea class="message-input" id="messageInput" placeholder="✨ Mesajınızı yazın veya sesli komut verin..." rows="1"></textarea>
                <button class="btn btn-primary" onclick="sendMessage()">📤</button>
            </div>
            
            <div class="loading" id="loading">
                <div class="loading-content">
                    <div class="spinner"></div>
                    <span>🧠 JARVIS düşünüyor...</span>
                </div>
            </div>

            <div class="controls">
                <button class="btn btn-success" id="activateBtn" onclick="toggleActivation()">🟢 Aktif Et</button>
                <button class="btn btn-secondary" id="testBtn" onclick="testConnection()">🔗 Test</button>
                <button class="btn voice-btn btn-danger" id="voiceBtn" onclick="toggleVoiceRecognition()">🎤</button>
            </div>

            <div class="mode-controls">
                <button class="btn btn-secondary" id="chatModeBtn" onclick="setMode('chat')">💬 Sohbet</button>
                <button class="btn btn-warning" id="codeModeBtn" onclick="setMode('code')">💻 Kod</button>
            </div>

            <div class="quick-commands">
                <button class="quick-btn" onclick="quickCommand('Saat kaç?')">⏰ Saat</button>
                <button class="quick-btn" onclick="quickCommand('Bugün ne günü?')">📅 Tarih</button>
                <button class="quick-btn" onclick="quickCommand('Ses artır')">🔊 Ses+</button>
                <button class="quick-btn" onclick="quickCommand('Ses azalt')">🔉 Ses-</button>
                <button class="quick-btn" onclick="quickCommand('Not al: Toplantı yarın saat 3te')">📝 Not</button>
                <button class="quick-btn" onclick="quickCommand('Youtube aç')">📺 YouTube</button>
                <button class="quick-btn" onclick="quickCommand('5 dakika sonra uyar')">⏰ Hatırlat</button>
                <button class="quick-btn" onclick="quickCommand('Yardım')">❓ Yardım</button>
                <button class="quick-btn" onclick="quickCommand('Sohbet geçmişi sil')">🗑️ Sohbet Sil</button>
                <button class="quick-btn" onclick="quickCommand('Kod geçmişi sil')">🗑️ Kod Sil</button>
                <button class="quick-btn" onclick="quickCommand('Instagram aç')">📱 Instagram</button>
                <button class="quick-btn" onclick="quickCommand('Discord aç')">🎮 Discord</button>
                <button class="quick-btn" onclick="quickCommand('Spotify aç')">🎵 Spotify</button>
                <button class="quick-btn" onclick="quickCommand('Excel aç')">📊 Excel</button>
                <button class="quick-btn" onclick="quickCommand('Klasör oluştur')">📁 Klasör</button>
                <button class="quick-btn" onclick="quickCommand('Fotoğrafları göster')">🖼️ Fotoğraf</button>
                <button class="quick-btn" onclick="quickCommand('İnternette python ara')">🔍 Arama</button>
                <button class="quick-btn" onclick="quickCommand('Yarın 14:00 doktor randevusu ekle')">👨‍⚕️ Randevu</button>
                <button class="quick-btn" onclick="quickCommand('Bu hafta hangi randevularım var')">📋 Randevu Listesi</button>
                <button class="quick-btn" onclick="quickCommand('Bilgisayarı kapat')">⚡ PC Kapat</button>
            </div>
        </div>
    </div>

    <script>
        let isActive = false;
        let isListening = false;
        let currentMode = 'chat';
        let recognition = null;
        let isConnected = false;
        let conversationHistory = [];

        // IP adresi otomatik belirleme
        function detectLocalIP() {
            // Mobil cihazın yerel IP'sini tahmin et
            const commonIPs = ['192.168.1', '192.168.0', '10.0.0', '172.16.0'];
            const serverIPInput = document.getElementById('serverIP');
            
            // Eğer boşsa varsayılan değer ata
            if (!serverIPInput.value) {
                serverIPInput.value = '192.168.1.100'; // En yaygın varsayılan
            }
        }

        // Bildirim gösterme fonksiyonu
        function showNotification(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = 'notification';
            notification.innerHTML = message;
            
            if (type === 'success') {
                notification.style.borderColor = 'var(--neon-green)';
                notification.style.color = 'var(--neon-green)';
            } else if (type === 'error') {
                notification.style.borderColor = 'var(--error-color)';
                notification.style.color = 'var(--error-color)';
            } else if (type === 'warning') {
                notification.style.borderColor = 'var(--warning-color)';
                notification.style.color = 'var(--warning-color)';
            }
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideInRight 0.5s ease reverse';
                setTimeout(() => notification.remove(), 500);
            }, 3000);
        }

        // Ses tanıma desteği
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.lang = 'tr-TR';
            recognition.continuous = false;
            recognition.interimResults = false;

            recognition.onresult = function(event) {
                const command = event.results[0][0].transcript;
                document.getElementById('messageInput').value = command;
                addMessage(`🎙️ Sesli komut: "${command}"`, 'user');
                sendMessage();
            };

            recognition.onerror = function(event) {
                console.error('Ses tanıma hatası:', event.error);
                stopListening();
                addMessage(`❌ Ses tanıma hatası: ${event.error}`, 'system');
                showNotification('🎤 Ses tanıma hatası!', 'error');
            };

            recognition.onend = function() {
                stopListening();
            };
        }

        function updateConnectionStatus(connected) {
            isConnected = connected;
            const dot = document.getElementById('connectionDot');
            const text = document.getElementById('connectionText');
            
            if (connected) {
                dot.classList.add('connected');
                text.textContent = '✅ PC\'ye Bağlandı';
                showNotification('🌐 PC bağlantısı başarılı!', 'success');
            } else {
                dot.classList.remove('connected');
                text.textContent = '❌ PC Bağlantısı Yok';
            }
        }

        async function testConnection() {
            const serverIP = document.getElementById('serverIP').value.trim();
            const serverPort = document.getElementById('serverPort').value.trim() || '5000';
            const testBtn = document.getElementById('testBtn');
            
            if (!serverIP) {
                addMessage('❌ Lütfen PC IP adresini girin!', 'system');
                showNotification('⚠️ IP adresi gerekli!', 'warning');
                return;
            }
            
            testBtn.textContent = '⏳ Test...';
            testBtn.disabled = true;
            
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 10000);
                
                // Flask sunucuya ping gönder
                const response = await fetch(`http://${serverIP}:${serverPort}/ping`, {
                    method: 'GET',
                    signal: controller.signal,
                    mode: 'cors'
                });
                
                clearTimeout(timeoutId);
                
                if (response.ok) {
                    const data = await response.text();
                    updateConnectionStatus(true);
                    addMessage(`✅ PC bağlantısı başarılı! JARVIS hazır.`, 'system');
                } else {
                    throw new Error(`HTTP ${response.status}`);
                }
            } catch (error) {
                updateConnectionStatus(false);
                if (error.name === 'AbortError') {
                    addMessage('❌ Bağlantı zaman aşımına uğradı (10 saniye)', 'system');
                    showNotification('⏱️ Bağlantı zaman aşımı!', 'error');
                } else {
                    addMessage(`❌ PC bağlantı hatası: ${error.message}`, 'system');
                    addMessage('💡 PC\'nizde JARVIS Python kodunun çalıştığından emin olun', 'system');
                    showNotification('🔴 PC bağlantı hatası!', 'error');
                }
            } finally {
                testBtn.textContent = '🔗 Test';
                testBtn.disabled = false;
            }
        }

        function toggleActivation() {
            if (!isConnected) {
                addMessage('❌ Önce PC bağlantısını test edin!', 'system');
                showNotification('⚠️ Önce PC\'ye bağlanın!', 'warning');
                return;
            }

            isActive = !isActive;
            updateStatus();
            
            if (isActive) {
                addMessage('🟢 JARVIS aktif edildi. Komutlarınızı bekliyorum!', 'jarvis');
                showNotification('🤖 JARVIS aktif!', 'success');
                // Aktivasyon komutunu PC'ye gönder
                sendToPC('babacık geldi');
            } else {
                addMessage('🔴 JARVIS pasif edildi. Görüşürüz!', 'jarvis');
                showNotification('👋 JARVIS pasif!', 'info');
                // Pasif komutunu PC'ye gönder
                sendToPC('kapan');
            }
        }

        function setMode(mode) {
            if (!isActive) {
                addMessage('❌ Önce asistanı aktif edin!', 'system');
                showNotification('⚠️ Önce aktif edin!', 'warning');
                return;
            }

            currentMode = mode;
            updateStatus();
            
            if (mode === 'chat') {
                addMessage('💬 Sohbet modu aktif. Benimle konuşabilirsiniz!', 'jarvis');
                showNotification('💬 Sohbet modu!', 'success');
                sendToPC('sohbet aç');
            } else {
                addMessage('💻 Kod modu aktif. Programlama sorularınızı sorabilirsiniz!', 'jarvis');
                showNotification('💻 Kod modu!', 'success');
                sendToPC('kod aç');
            }
        }

        function updateStatus() {
            const statusBar = document.getElementById('statusBar');
            const statusText = document.getElementById('statusText');
            const activateBtn = document.getElementById('activateBtn');
            const chatModeBtn = document.getElementById('chatModeBtn');
            const codeModeBtn = document.getElementById('codeModeBtn');
            
            chatModeBtn.className = 'btn btn-secondary';
            codeModeBtn.className = 'btn btn-warning';
            
            if (isActive) {
                if (currentMode === 'chat') {
                    statusBar.className = 'status-bar chat-mode';
                    statusText.textContent = '💬 SOHBET MODU - Aktif';
                    chatModeBtn.className = 'btn btn-primary';
                } else {
                    statusBar.className = 'status-bar code-mode';
                    statusText.textContent = '💻 KOD MODU - Aktif';
                    codeModeBtn.className = 'btn btn-primary';
                }
                activateBtn.textContent = '🔴 Pasif Et';
                activateBtn.className = 'btn btn-danger';
            } else {
                statusBar.className = 'status-bar passive';
                statusText.textContent = '🔴 Asistan Pasif';
                activateBtn.textContent = '🟢 Aktif Et';
                activateBtn.className = 'btn btn-success';
            }
        }

        function toggleVoiceRecognition() {
            if (!recognition) {
                addMessage('❌ Tarayıcınız ses tanımayı desteklemiyor.', 'system');
                showNotification('🚫 Ses tanıma yok!', 'error');
                return;
            }

            if (!isActive) {
                addMessage('❌ Önce asistanı aktif edin!', 'system');
                showNotification('⚠️ Önce aktif edin!', 'warning');
                return;
            }

            if (isListening) {
                stopListening();
            } else {
                startListening();
            }
        }

        function startListening() {
            isListening = true;
            const voiceBtn = document.getElementById('voiceBtn');
            voiceBtn.classList.add('listening');
            voiceBtn.innerHTML = '🔴';
            
            addMessage('🎤 Dinliyorum... Konuşabilirsiniz.', 'system');
            showNotification('🎤 Ses kaydı başladı!', 'info');
            
            try {
                recognition.start();
            } catch (error) {
                stopListening();
                addMessage('❌ Ses tanıma başlatılamadı', 'system');
                showNotification('🚫 Ses tanıma hatası!', 'error');
            }
        }

        function stopListening() {
            isListening = false;
            const voiceBtn = document.getElementById('voiceBtn');
            voiceBtn.classList.remove('listening');
            voiceBtn.innerHTML = '🎤';
            
            if (recognition) {
                try {
                    recognition.stop();
                } catch (error) {
                    console.warn('Recognition stop error:', error);
                }
            }
        }

        async function sendMessage() {
            if (!isActive) {
                addMessage('❌ Asistanı önce aktif edin!', 'system');
                showNotification('⚠️ Asistan pasif!', 'warning');
                return;
            }

            if (!isConnected) {
                addMessage('❌ PC bağlantısı yok!', 'system');
                showNotification('🔴 PC bağlantısı yok!', 'error');
                return;
            }

            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;

            if (!message.startsWith('🎙️')) {
                addMessage(message, 'user');
            }
            
            input.value = '';
            autoResize(input);
            
            showLoading(true);
            
            try {
                await sendToPC(message.replace('🎙️ Sesli komut: "', '').replace('"', ''));
            } catch (error) {
                addMessage(`❌ Hata: ${error.message}`, 'system');
                showNotification('🚫 Mesaj gönderilemedi!', 'error');
            } finally {
                showLoading(false);
            }
        }

        async function sendToPC(message) {
            const serverIP = document.getElementById('serverIP').value || '192.168.1.100';
            const serverPort = document.getElementById('serverPort').value || '5000';

            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 30000);

                const response = await fetch(`http://${serverIP}:${serverPort}/command`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        command: message,
                        mode: currentMode
                    }),
                    signal: controller.signal
                });

                clearTimeout(timeoutId);

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }

                const data = await response.json();
                const reply = data.response?.trim() || 'Komut PC\'ye gönderildi.';
                
                addMessage(reply, 'jarvis');
                
                conversationHistory.push({
                    user: message,
                    jarvis: reply,
                    mode: currentMode,
                    timestamp: new Date().toISOString()
                });

                if (conversationHistory.length > 20) {
                    conversationHistory = conversationHistory.slice(-20);
                }

                // Sesli yanıt
                if ('speechSynthesis' in window && reply.length < 200) {
                    try {
                        speechSynthesis.cancel();
                        
                        const utterance = new SpeechSynthesisUtterance(reply);
                        utterance.lang = 'tr-TR';
                        utterance.rate = 0.85;
                        utterance.pitch = 1.0;
                        utterance.volume = 0.8;
                        
                        const voices = speechSynthesis.getVoices();
                        const turkishVoice = voices.find(voice => 
                            voice.lang.includes('tr') || voice.name.includes('Turkish')
                        );
                        if (turkishVoice) {
                            utterance.voice = turkishVoice;
                        }
                        
                        speechSynthesis.speak(utterance);
                    } catch (speechError) {
                        console.warn('Sesli yanıt hatası:', speechError);
                    }
                }

            } catch (error) {
                if (error.name === 'AbortError') {
                    throw new Error('PC yanıt vermedi (30 saniye)');
                } else {
                    throw new Error(`PC bağlantı hatası: ${error.message}`);
                }
            }
        }

        function quickCommand(command) {
            if (!isActive) {
                if (isConnected) {
                    toggleActivation();
                    setTimeout(() => {
                        if (isActive) {
                            document.getElementById('messageInput').value = command;
                            sendMessage();
                        }
                    }, 1500);
                } else {
                    addMessage('❌ Önce PC bağlantısını test edin!', 'system');
                    showNotification('⚠️ Önce PC\'ye bağlanın!', 'warning');
                }
            } else {
                document.getElementById('messageInput').value = command;
                sendMessage();
            }
        }

        function addMessage(text, sender) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            
            let className = 'message ';
            switch(sender) {
                case 'user':
                    className += 'user-message';
                    break;
                case 'jarvis':
                    className += 'jarvis-message';
                    break;
                case 'system':
                    className += 'system-message';
                    break;
            }
            
            messageDiv.className = className;
            
            const now = new Date();
            const timestamp = now.toLocaleTimeString('tr-TR', { 
                hour: '2-digit', 
                minute: '2-digit',
                second: '2-digit'
            });
            
            if (sender === 'system') {
                messageDiv.innerHTML = `<strong>${text}</strong><br><small style="opacity: 0.6; font-size: 11px;">${timestamp}</small>`;
            } else {
                const senderIcon = sender === 'user' ? '👤' : '🤖';
                messageDiv.innerHTML = `${senderIcon} ${text}<br><small style="opacity: 0.6; font-size: 11px;">${timestamp}</small>`;
            }
            
            chatContainer.appendChild(messageDiv);
            
            setTimeout(() => {
                chatContainer.scrollTo({
                    top: chatContainer.scrollHeight,
                    behavior: 'smooth'
                });
            }, 100);
        }

        function showLoading(show) {
            const loading = document.getElementById('loading');
            loading.style.display = show ? 'block' : 'none';
        }

        function autoResize(textarea) {
            textarea.style.height = 'auto';
            textarea.style.height = Math.min(textarea.scrollHeight, 140) + 'px';
        }

        // Event Listeners
        document.getElementById('messageInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        document.getElementById('messageInput').addEventListener('input', function(e) {
            autoResize(e.target);
        });

        // Sayfa yüklendiğinde
        window.addEventListener('load', function() {
            detectLocalIP();
            
            setTimeout(() => {
                addMessage('🚀 JARVIS Mobil Edition hazır!', 'system');
                addMessage('📱 PC\'nizdeki JARVIS Python kodunuz çalışır durumdayken:', 'system');
                addMessage('🔧 1. PC IP adresinizi girin\n🔗 2. Test butonuna basın\n🟢 3. Aktif Et\'e basın\n💬 4. Sohbet veya Kod modu seçin', 'system');
            }, 1000);

            updateStatus();
            
            if ('speechSynthesis' in window) {
                speechSynthesis.getVoices();
                speechSynthesis.onvoiceschanged = () => {
                    const voices = speechSynthesis.getVoices();
                    console.log('Mevcut sesler:', voices.length);
                };
            }
        });

        // Klavye kısayolları
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                toggleVoiceRecognition();
            }
            
            if (e.ctrlKey && e.key === '/') {
                e.preventDefault();
                quickCommand('Yardım');
            }
            
            if (e.ctrlKey && e.key === 't') {
                e.preventDefault();
                testConnection();
            }
            
            if (e.ctrlKey && e.key === '1') {
                e.preventDefault();
                setMode('chat');
            }
            
            if (e.ctrlKey && e.key === '2') {
                e.preventDefault();
                setMode('code');
            }
            
            if (e.ctrlKey && e.key === ' ') {
                e.preventDefault();
                toggleActivation();
            }
            
            if (e.key === 'Escape' && isListening) {
                e.preventDefault();
                stopListening();
            }
        });

        // Sayfa görünürlük değişikliklerini izle
        document.addEventListener('visibilitychange', function() {
            if (document.hidden) {
                if (isListening) {
                    stopListening();
                }
                if ('speechSynthesis' in window) {
                    speechSynthesis.cancel();
                }
            }
        });

        // Ağ durumunu izle
        window.addEventListener('online', function() {
            showNotification('🌐 İnternet bağlantısı geri geldi!', 'success');
            if (isConnected) {
                setTimeout(testConnection, 1000);
            }
        });

        window.addEventListener('offline', function() {
            showNotification('📡 İnternet bağlantısı kesildi!', 'error');
            updateConnectionStatus(false);
        });

        // Hata yakalama
        window.addEventListener('error', function(e) {
            console.error('Global hata:', e.error);
            showNotification('⚠️ Bir hata oluştu!', 'error');
        });

        window.addEventListener('unhandledrejection', function(e) {
            console.error('Promise hatası:', e.reason);
            showNotification('🚫 Bağlantı hatası!', 'error');
        });

        window.addEventListener('beforeunload', function() {
            if (isListening) {
                stopListening();
            }
            if ('speechSynthesis' in window) {
                speechSynthesis.cancel();
            }
        });
    </script>
</body>
</html><!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVIS - AI Assistant</title>
    <meta name="theme-color" content="#000000">
    <link rel="manifest" href="data:application/json,{&quot;name&quot;:&quot;JARVIS AI Assistant&quot;,&quot;short_name&quot;:&quot;JARVIS&quot;,&quot;start_url&quot;:&quot;.&quot;,&quot;display&quot;:&quot;standalone&quot;,&quot;theme_color&quot;:&quot;#000000&quot;,&quot;background_color&quot;:&quot;#000000&quot;}">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-bg: #000000;
            --secondary-bg: #0a0a0a;
            --tertiary-bg: #1a1a1a;
            --quaternary-bg: #2a2a2a;
            --glass-bg: rgba(15, 15, 15, 0.85);
            --dark-glass: rgba(5, 5, 5, 0.9);
            --primary-text: #ffffff;
            --secondary-text: #a0a0a0;
            --tertiary-text: #707070;
            --accent-text: #00d4ff;
            --success-color: #00ff88;
            --warning-color: #ff9500;
            --error-color: #ff3366;
            --neon-blue: #0099ff;
            --neon-purple: #6644cc;
            --neon-pink: #ff4488;
            --neon-green: #00ff88;
            --neon-cyan: #00ffff;
            --border-dark: rgba(255, 255, 255, 0.05);
            --border-light: rgba(255, 255, 255, 0.1);
            --shadow-dark: rgba(0, 0, 0, 0.8);
            --shadow-neon: rgba(0, 153, 255, 0.3);
        }

        body {
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--primary-bg);
            color: var(--primary-text);
            min-height: 100vh;
            padding: 0;
            overflow-x: hidden;
            position: relative;
        }

        /* Ultra dark animated background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 15% 85%, rgba(0, 153, 255, 0.03) 0%, transparent 60%),
                radial-gradient(circle at 85% 15%, rgba(102, 68, 204, 0.03) 0%, transparent 60%),
                radial-gradient(circle at 50% 50%, rgba(255, 68, 136, 0.02) 0%, transparent 70%),
                linear-gradient(135deg, rgba(0, 0, 0, 0.95) 0%, rgba(10, 10, 10, 0.95) 100%);
            z-index: -1;
            animation: bgFloat 25s ease-in-out infinite;
        }

        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 98px,
                    rgba(0, 153, 255, 0.01) 100px
                ),
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 98px,
                    rgba(102, 68, 204, 0.01) 100px
                );
            z-index: -1;
            opacity: 0.3;
        }

        @keyframes bgFloat {
            0%, 100% { transform: translate(0, 0) rotate(0deg); opacity: 0.7; }
            25% { transform: translate(-15px, -10px) rotate(0.5deg); opacity: 0.9; }
            50% { transform: translate(10px, -15px) rotate(-0.5deg); opacity: 0.8; }
            75% { transform: translate(-10px, 10px) rotate(0.3deg); opacity: 0.9; }
        }

        .container {
            max-width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            position: relative;
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.9) 0%, rgba(10, 10, 10, 0.95) 100%);
        }

        .header {
            padding: 25px 20px;
            text-align: center;
            background: var(--dark-glass);
            backdrop-filter: blur(25px);
            border-bottom: 1px solid var(--border-dark);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px var(--shadow-dark);
        }

        .logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            margin-bottom: 12px;
        }

        .logo-icon {
            width: 55px;
            height: 55px;
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            animation: logoFloat 4s ease-in-out infinite;
            box-shadow: 
                0 0 20px rgba(0, 153, 255, 0.4),
                inset 0 0 20px rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(0, 153, 255, 0.3);
        }

        @keyframes logoFloat {
            0%, 100% { 
                transform: translateY(0px) rotate(0deg) scale(1); 
                box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);
            }
            50% { 
                transform: translateY(-8px) rotate(3deg) scale(1.05); 
                box-shadow: 0 0 30px rgba(0, 153, 255, 0.6);
            }
        }

        .logo {
            font-size: 2.4rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple), var(--neon-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 3px;
            text-shadow: 0 0 30px rgba(0, 153, 255, 0.5);
            animation: textGlow 3s ease-in-out infinite alternate;
        }

        @keyframes textGlow {
            from { filter: brightness(1) drop-shadow(0 0 5px rgba(0, 153, 255, 0.5)); }
            to { filter: brightness(1.2) drop-shadow(0 0 15px rgba(0, 153, 255, 0.8)); }
        }

        .subtitle {
            font-size: 0.85rem;
            color: var(--secondary-text);
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            opacity: 0.8;
        }

        .status-bar {
            padding: 18px 25px;
            margin: 15px 20px;
            border-radius: 25px;
            text-align: center;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-dark);
            background: var(--tertiary-bg);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        .status-bar.active {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.15), rgba(0, 153, 255, 0.15));
            border: 1px solid rgba(0, 255, 136, 0.3);
            box-shadow: 
                0 0 40px rgba(0, 255, 136, 0.3),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-green);
        }

        .status-bar.passive {
            background: linear-gradient(135deg, rgba(102, 68, 204, 0.15), rgba(255, 68, 136, 0.15));
            border: 1px solid rgba(102, 68, 204, 0.3);
            box-shadow: 
                0 0 40px rgba(102, 68, 204, 0.3),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-purple);
        }

        .status-bar.chat-mode {
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.15), rgba(0, 255, 255, 0.15));
            border: 1px solid rgba(0, 153, 255, 0.4);
            box-shadow: 
                0 0 40px rgba(0, 153, 255, 0.4),
                0 8px 32px var(--shadow-dark);
            color: var(--neon-cyan);
        }

        .status-bar.code-mode {
            background: linear-gradient(135deg, rgba(255, 149, 0, 0.15), rgba(255, 68, 136, 0.15));
            border: 1px solid rgba(255, 149, 0, 0.4);
            box-shadow: 
                0 0 40px rgba(255, 149, 0, 0.4),
                0 8px 32px var(--shadow-dark);
            color: var(--warning-color);
        }

        .chat-container {
            flex: 1;
            padding: 25px;
            overflow-y: auto;
            max-height: calc(100vh - 350px);
            scroll-behavior: smooth;
            background: rgba(0, 0, 0, 0.2);
        }

        .message {
            margin-bottom: 25px;
            padding: 20px 25px;
            border-radius: 28px;
            max-width: 85%;
            word-wrap: break-word;
            animation: messageSlide 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(15px);
            border: 1px solid var(--border-dark);
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 32px var(--shadow-dark);
        }

        .message::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        }

        .message::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.03) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
        }

        .message:hover::after {
            opacity: 1;
        }

        @keyframes messageSlide {
            from { 
                opacity: 0; 
                transform: translateY(40px) scale(0.9); 
                filter: blur(5px);
            }
            to { 
                opacity: 1; 
                transform: translateY(0) scale(1); 
                filter: blur(0);
            }
        }

        .user-message {
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(102, 68, 204, 0.1));
            margin-left: auto;
            text-align: right;
            border-left: 3px solid var(--neon-blue);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(0, 153, 255, 0.2);
        }

        .jarvis-message {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.08), rgba(0, 153, 255, 0.08));
            margin-right: auto;
            border-left: 3px solid var(--neon-green);
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(0, 255, 136, 0.2);
        }

        .system-message {
            background: linear-gradient(135deg, rgba(255, 149, 0, 0.08), rgba(255, 68, 136, 0.08));
            margin: 0 auto;
            text-align: center;
            font-style: italic;
            border-left: 3px solid var(--warning-color);
            max-width: 75%;
            box-shadow: 
                0 8px 32px var(--shadow-dark),
                -5px 0 15px rgba(255, 149, 0, 0.2);
        }

        .input-section {
            background: var(--dark-glass);
            backdrop-filter: blur(25px);
            padding: 30px 25px;
            border-top: 1px solid var(--border-dark);
            position: sticky;
            bottom: 0;
            box-shadow: 0 -8px 32px var(--shadow-dark);
        }

        .server-config {
            margin-bottom: 25px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 20px;
            border: 1px solid var(--border-dark);
            backdrop-filter: blur(10px);
            box-shadow: 
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 4px 20px var(--shadow-dark);
        }

        .config-row {
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
            align-items: center;
        }

        .config-row:last-child {
            margin-bottom: 0;
        }

        .config-input {
            flex: 1;
            padding: 15px 20px;
            border: 1px solid var(--border-light);
            border-radius: 15px;
            background: rgba(0, 0, 0, 0.6);
            color: var(--primary-text);
            font-size: 14px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        .config-input:focus {
            outline: none;
            border-color: var(--neon-blue);
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 
                0 0 25px rgba(0, 153, 255, 0.3),
                inset 0 2px 10px rgba(0, 0, 0, 0.7);
            transform: translateY(-1px);
        }

        .config-input::placeholder {
            color: var(--tertiary-text);
        }

        .input-group {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            align-items: flex-end;
        }

        .message-input {
            flex: 1;
            padding: 18px 25px;
            border: 1px solid var(--border-light);
            border-radius: 28px;
            background: rgba(0, 0, 0, 0.6);
            color: var(--primary-text);
            font-size: 16px;
            backdrop-filter: blur(15px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            resize: none;
            min-height: 56px;
            max-height: 140px;
            box-shadow: 
                inset 0 2px 15px rgba(0, 0, 0, 0.6),
                0 4px 20px var(--shadow-dark);
        }

        .message-input:focus {
            outline: none;
            border-color: var(--neon-blue);
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 
                0 0 30px rgba(0, 153, 255, 0.4),
                inset 0 2px 15px rgba(0, 0, 0, 0.8);
            transform: translateY(-3px);
        }

        .message-input::placeholder {
            color: var(--tertiary-text);
        }

        .btn {
            padding: 18px 28px;
            border: none;
            border-radius: 22px;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-transform: uppercase;
            letter-spacing: 1.2px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(15px);
            border: 1px solid var(--border-light);
            box-shadow: 0 8px 32px var(--shadow-dark);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
            transition: left 0.6s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn:active {
            transform: scale(0.95);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--neon-blue), rgba(0, 153, 255, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(0, 153, 255, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(0, 153, 255, 0.5);
        }

        .btn-primary:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(0, 153, 255, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-secondary {
            background: linear-gradient(135deg, var(--neon-purple), rgba(102, 68, 204, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(102, 68, 204, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(102, 68, 204, 0.5);
        }

        .btn-secondary:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(102, 68, 204, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-success {
            background: linear-gradient(135deg, var(--neon-green), rgba(0, 255, 136, 0.7));
            color: var(--primary-bg);
            box-shadow: 
                0 0 25px rgba(0, 255, 136, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(0, 255, 136, 0.5);
        }

        .btn-success:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 0 35px rgba(0, 255, 136, 0.6),
                0 12px 40px var(--shadow-dark);
        }

        .btn-danger {
            background: linear-gradient(135deg, var(--error-color), rgba(255, 51, 102, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(255, 51, 102, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(255, 51, 102, 0.5);
        }

        .btn-warning {
            background: linear-gradient(135deg, var(--warning-color), rgba(255, 149, 0, 0.7));
            color: white;
            box-shadow: 
                0 0 25px rgba(255, 149, 0, 0.4),
                0 8px 32px var(--shadow-dark);
            border-color: rgba(255, 149, 0, 0.5);
        }

        .controls {
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 15px;
            margin-bottom: 25px;
        }

        .mode-controls {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }

        .voice-btn {
            width: 65px;
            height: 65px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            position: relative;
        }

        .voice-btn.listening {
            animation: voicePulse 1.8s ease-in-out infinite;
        }

        @keyframes voicePulse {
            0% { 
                transform: scale(1); 
                box-shadow: 
                    0 0 25px rgba(255, 51, 102, 0.6),
                    0 0 0 0 rgba(255, 51, 102, 0.7); 
            }
            70% { 
                transform: scale(1.1); 
                box-shadow: 
                    0 0 35px rgba(255, 51, 102, 0.8),
                    0 0 0 25px rgba(255, 51, 102, 0); 
            }
            100% { 
                transform: scale(1); 
                box-shadow: 
                    0 0 25px rgba(255, 51, 102, 0.6),
                    0 0 0 0 rgba(255, 51, 102, 0); 
            }
        }

        .quick-commands {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
            gap: 15px;
        }

        .quick-btn {
            padding: 15px 20px;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--border-light);
            border-radius: 18px;
            color: var(--primary-text);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 13px;
            font-weight: 600;
            backdrop-filter: blur(15px);
            text-align: center;
            box-shadow: 
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 4px 20px var(--shadow-dark);
            position: relative;
            overflow: hidden;
        }

        .quick-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(102, 68, 204, 0.1));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .quick-btn:hover {
            background: rgba(0, 0, 0, 0.8);
            transform: translateY(-3px);
            box-shadow: 
                0 0 20px rgba(0, 153, 255, 0.3),
                0 8px 30px var(--shadow-dark);
            border-color: rgba(0, 153, 255, 0.4);
        }

        .quick-btn:hover::before {
            opacity: 1;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 25px;
            margin: 25px 0;
        }

        .loading-content {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            color: var(--neon-blue);
            font-weight: 600;
            font-size: 1.1rem;
        }

        .spinner {
            width: 28px;
            height: 28px;
            border: 4px solid rgba(0, 153, 255, 0.2);
            border-radius: 50%;
            border-top-color: var(--neon-blue);
            animation: spin 1.2s linear infinite;
            box-shadow: 0 0 15px rgba(0, 153, 255, 0.4);
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .connection-status {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
            margin-top: 12px;
            justify-content: center;
            font-weight: 600;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--error-color);
            animation: statusBlink 2.5s ease-in-out infinite;
            box-shadow: 0 0 10px var(--error-color);
        }

        .status-dot.connected {
            background: var(--neon-green);
            box-shadow: 0 0 15px var(--neon-green);
            animation: none;
        }

        @keyframes statusBlink {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.8); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .logo {
                font-size: 2rem;
            }
            
            .controls {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            
            .input-group {
                flex-direction: column;
                gap: 12px;
            }
            
            .config-row {
                flex-direction: column;
                align-items: stretch;
            }
            
            .voice-btn {
                width: 100%;
                height: 55px;
                border-radius: 28px;
            }

            .quick-commands {
                grid-template-columns: repeat(2, 1fr);
            }

            .chat-container {
                padding: 20px;
                max-height: calc(100vh - 380px);
            }
        }

        @media (max-width: 480px) {
            .header {
                padding: 20px 15px;
            }
            
            .chat-container {
                padding: 15px;
                max-height: calc(100vh - 400px);
            }
            
            .input-section {
                padding: 25px 15px;
            }
            
            .message {
                max-width: 95%;
                padding: 16px 20px;
            }

            .logo {
                font-size: 1.8rem;
            }

            .quick-commands {
                grid-template-columns: 1fr;
            }
        }

        /* Ultra dark scrollbar */
        .chat-container::-webkit-scrollbar {
            width: 8px;
        }

        .chat-container::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 4px;
        }

        .chat-container::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, rgba(0, 153, 255, 0.6), rgba(102, 68, 204, 0.6));
            border-radius: 4px;
            box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.8);
        }

        .chat-container::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, rgba(0, 153, 255, 0.8), rgba(102, 68, 204, 0.8));
            box-shadow: 0 0 10px rgba(0, 153, 255, 0.5);
        }

        /* Loading pulse effect */
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Advanced hover effects */
        .message:hover {
            transform: translateY(-2px);
            box-shadow: 
                0 12px 40px var(--shadow-dark),
                0 0 20px rgba(0, 153, 255, 0.2);
        }

        /* Notification styles */
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: rgba(0, 0, 0, 0.9);
            border: 1px solid var(--neon-green);
            border-radius: 12px;
            color: var(--neon-green);
            font-weight: 600;
            backdrop-filter: blur(15px);
            box-shadow: 0 8px 32px var(--shadow-dark);
            z-index: 1000;
            animation: slideInRight 0.5s ease;
        }

        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-container">
                <div class="logo-icon">🤖</div>
                <div>
                    <div class="logo">JARVIS</div>
                    <div class="subtitle">AI ASSISTANT</div>
                </div>
            </div>
        </div>

        <div class="status-bar passive" id="statusBar">
            <span id="statusText">🔴 Asistan Pasif - Bağlantı Bekleniyor</span>
        </div>

        <div class="chat-container" id="chatContainer">
            <div class="message system-message">
                <strong>🚀 JARVIS AI Assistant v2.0 - Ultra Dark Edition</strong><br>
                PC'nizdeki JARVIS Python koduna bağlanmak için aşağıdaki adımları takip edin:<br>
                <br>
                <strong>📋 Bağlantı Adımları:</strong><br>
                1️⃣ PC'nizde JARVIS Python kodunu çalıştırın<br>
                2️⃣ PC'nizin IP adresini öğrenin (cmd > ipconfig)<br>
                3️⃣ IP adresini aşağıya girin<br>
                4️⃣ "Test" butonuna basın<br>
                5️⃣ "Aktif Et" ile asistanı başlatın<br>
                <br>
                <small style="opacity: 0.7;">💡 Python kodunuz çalışırken mobil cihazınızdan tüm JARVIS özelliklerini kontrol edebilirsiniz.</small>
            </div>
        </div>

        <div class="input-section">
            <div class="server-config">
                <div class="config-row">
                    <input type="text" class="config-input" id="serverIP" placeholder="🌐 PC IP Adresi (örn: 192.168.1.100)" value="">
                    <input type="text" class="config-input" id="serverPort" placeholder="🔌 Port (Flask sunucu portu)" value="5000">
                </div>
                <div class="connection-status">
                    <div class="status-dot" id="connectionDot"></div>
                    <span id="connectionText">Bağlantı Bekleniyor</span>
                </div>
            </div>

            <div class="input-group">
                <textarea class="message-input" id="messageInput" placeholder="✨ Mesajınızı yazın veya sesli komut verin..." rows="1"></textarea>
                <button class="btn btn-primary" onclick="sendMessage()">📤</button>
            </div>
            
            <div class="loading" id="loading">
                <div class="loading-content">
                    <div class="spinner"></div>
                    <span>🧠 JARVIS düşünüyor...</span>
                </div>
            </div>

            <div class="controls">
                <button class="btn btn-success" id="activateBtn" onclick="toggleActivation()">🟢 Aktif Et</button>
                <button class="btn btn-secondary" id="testBtn" onclick="testConnection()">🔗 Test</button>
                <button class="btn voice-btn btn-danger" id="voiceBtn" onclick="toggleVoiceRecognition()">🎤</button>
            </div>

            <div class="mode-controls">
                <button class="btn btn-secondary" id="chatModeBtn" onclick="setMode('chat')">💬 Sohbet</button>
                <button class="btn btn-warning" id="codeModeBtn" onclick="setMode('code')">💻 Kod</button>
            </div>

            <div class="quick-commands">
                <button class="quick-btn" onclick="quickCommand('Saat kaç?')">⏰ Saat</button>
                <button class="quick-btn" onclick="quickCommand('Bugün ne günü?')">📅 Tarih</button>
                <button class="quick-btn" onclick="quickCommand('Ses artır')">🔊 Ses+</button>
                <button class="quick-btn" onclick="quickCommand('Ses azalt')">🔉 Ses-</button>
                <button class="quick-btn" onclick="quickCommand('Not al: Toplantı yarın saat 3te')">📝 Not</button>
                <button class="quick-btn" onclick="quickCommand('Youtube aç')">📺 YouTube</button>
                <button class="quick-btn" onclick="quickCommand('5 dakika sonra uyar')">⏰ Hatırlat</button>
                <button class="quick-btn" onclick="quickCommand('Yardım')">❓ Yardım</button>
                <button class="quick-btn" onclick="quickCommand('Sohbet geçmişi sil')">🗑️ Sohbet Sil</button>
                <button class="quick-btn" onclick="quickCommand('Kod geçmişi sil')">🗑️ Kod Sil</button>
                <button class="quick-btn" onclick="quickCommand('Instagram aç')">📱 Instagram</button>
                <button class="quick-btn" onclick="quickCommand('Discord aç')">🎮 Discord</button>
                <button class="quick-btn" onclick="quickCommand('Spotify aç')">🎵 Spotify</button>
                <button class="quick-btn" onclick="quickCommand('Excel aç')">📊 Excel</button>
                <button class="quick-btn" onclick="quickCommand('Klasör oluştur')">📁 Klasör</button>
                <button class="quick-btn" onclick="quickCommand('Fotoğrafları göster')">🖼️ Fotoğraf</button>
                <button class="quick-btn" onclick="quickCommand('İnternette python ara')">🔍 Arama</button>
                <button class="quick-btn" onclick="quickCommand('Yarın 14:00 doktor randevusu ekle')">👨‍⚕️ Randevu</button>
                <button class="quick-btn" onclick="quickCommand('Bu hafta hangi randevularım var')">📋 Randevu Listesi</button>
                <button class="quick-btn" onclick="quickCommand('Bilgisayarı kapat')">⚡ PC Kapat</button>
            </div>
        </div>
    </div>

    <script>
        let isActive = false;
        let isListening = false;
        let currentMode = 'chat';
        let recognition = null;
        let isConnected = false;
        let conversationHistory = [];

        // IP adresi otomatik belirleme
        function detectLocalIP() {
            // Mobil cihazın yerel IP'sini tahmin et
            const commonIPs = ['192.168.1', '192.168.0', '10.0.0', '172.16.0'];
            const serverIPInput = document.getElementById('serverIP');
            
            // Eğer boşsa varsayılan değer ata
            if (!serverIPInput.value) {
                serverIPInput.value = '192.168.1.100'; // En yaygın varsayılan
            }
        }

        // Bildirim gösterme fonksiyonu
        function showNotification(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = 'notification';
            notification.innerHTML = message;
            
            if (type === 'success') {
                notification.style.borderColor = 'var(--neon-green)';
                notification.style.color = 'var(--neon-green)';
            } else if (type === 'error') {
                notification.style.borderColor = 'var(--error-color)';
                notification.style.color = 'var(--error-color)';
            } else if (type === 'warning') {
                notification.style.borderColor = 'var(--warning-color)';
                notification.style.color = 'var(--warning-color)';
            }
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideInRight 0.5s ease reverse';
                setTimeout(() => notification.remove(), 500);
            }, 3000);
        }

        // Ses tanıma desteği
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.lang = 'tr-TR';
            recognition.continuous = false;
            recognition.interimResults = false;

            recognition.onresult = function(event) {
                const command = event.results[0][0].transcript;
                document.getElementById('messageInput').value = command;
                addMessage(`🎙️ Sesli komut: "${command}"`, 'user');
                sendMessage();
            };

            recognition.onerror = function(event) {
                console.error('Ses tanıma hatası:', event.error);
                stopListening();
                addMessage(`❌ Ses tanıma hatası: ${event.error}`, 'system');
                showNotification('🎤 Ses tanıma hatası!', 'error');
            };

            recognition.onend = function() {
                stopListening();
            };
        }

        function updateConnectionStatus(connected) {
            isConnected = connected;
            const dot = document.getElementById('connectionDot');
            const text = document.getElementById('connectionText');
            
            if (connected) {
                dot.classList.add('connected');
                text.textContent = '✅ PC\'ye Bağlandı';
                showNotification('🌐 PC bağlantısı başarılı!', 'success');
            } else {
                dot.classList.remove('connected');
                text.textContent = '❌ PC Bağlantısı Yok';
            }
        }

        async function testConnection() {
            const serverIP = document.getElementById('serverIP').value.trim();
            const serverPort = document.getElementById('serverPort').value.trim() || '5000';
            const testBtn = document.getElementById('testBtn');
            
            if (!serverIP) {
                addMessage('❌ Lütfen PC IP adresini girin!', 'system');
                showNotification('⚠️ IP adresi gerekli!', 'warning');
                return;
            }
            
            testBtn.textContent = '⏳ Test...';
            testBtn.disabled = true;
            
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 10000);
                
                // Flask sunucuya ping gönder
                const response = await fetch(`http://${serverIP}:${serverPort}/ping`, {
                    method: 'GET',
                    signal: controller.signal,
                    mode: 'cors'
                });
                
                clearTimeout(timeoutId);
                
                if (response.ok) {
                    const data = await response.text();
                    updateConnectionStatus(true);
                    addMessage(`✅ PC bağlantısı başarılı! JARVIS hazır.`, 'system');
                } else {
                    throw new Error(`HTTP ${response.status}`);
                }
            } catch (error) {
                updateConnectionStatus(false);
                if (error.name === 'AbortError') {
                    addMessage('❌ Bağlantı zaman aşımına uğradı (10 saniye)', 'system');
                    showNotification('⏱️ Bağlantı zaman aşımı!', 'error');
                } else {
                    addMessage(`❌ PC bağlantı hatası: ${error.message}`, 'system');
                    addMessage('💡 PC\'nizde JARVIS Python kodunun çalıştığından emin olun', 'system');
                    showNotification('🔴 PC bağlantı hatası!', 'error');
                }
            } finally {
                testBtn.textContent = '🔗 Test';
                testBtn.disabled = false;
            }
        }

        function toggleActivation() {
            if (!isConnected) {
                addMessage('❌ Önce PC bağlantısını test edin!', 'system');
                showNotification('⚠️ Önce PC\'ye bağlanın!', 'warning');
                return;
            }

            isActive = !isActive;
            updateStatus();
            
            if (isActive) {
                addMessage('🟢 JARVIS aktif edildi. Komutlarınızı bekliyorum!', 'jarvis');
                showNotification('🤖 JARVIS aktif!', 'success');
                // Aktivasyon komutunu PC'ye gönder
                sendToPC('babacık geldi');
            } else {
                addMessage('🔴 JARVIS pasif edildi. Görüşürüz!', 'jarvis');
                showNotification('👋 JARVIS pasif!', 'info');
                // Pasif komutunu PC'ye gönder
                sendToPC('kapan');
            }
        }

        function setMode(mode) {
            if (!isActive) {
                addMessage('❌ Önce asistanı aktif edin!', 'system');
                showNotification('⚠️ Önce aktif edin!', 'warning');
                return;
            }

            currentMode = mode;
            updateStatus();
            
            if (mode === 'chat') {
                addMessage('💬 Sohbet modu aktif. Benimle konuşabilirsiniz!', 'jarvis');
                showNotification('💬 Sohbet modu!', 'success');
                sendToPC('sohbet aç');
            } else {
                addMessage('💻 Kod modu aktif. Programlama sorularınızı sorabilirsiniz!', 'jarvis');
                showNotification('💻 Kod modu!', 'success');
                sendToPC('kod aç');
            }
        }

        function updateStatus() {
            const statusBar = document.getElementById('statusBar');
            const statusText = document.getElementById('statusText');
            const activateBtn = document.getElementById('activateBtn');
            const chatModeBtn = document.getElementById('chatModeBtn');
            const codeModeBtn = document.getElementById('codeModeBtn');
            
            chatModeBtn.className = 'btn btn-secondary';
            codeModeBtn.className = 'btn btn-warning';
            
            if (isActive) {
                if (currentMode === 'chat') {
                    statusBar.className = 'status-bar chat-mode';
                    statusText.textContent = '💬 SOHBET MODU - Aktif';
                    chatModeBtn.className = 'btn btn-primary';
                } else {
                    statusBar.className = 'status-bar code-mode';
                    statusText.textContent = '💻 KOD MODU - Aktif';
                    codeModeBtn.className = 'btn btn-primary';
                }
                activateBtn.textContent = '🔴 Pasif Et';
                activateBtn.className = 'btn btn-danger';
            } else {
                statusBar.className = 'status-bar passive';
                statusText.textContent = '🔴 Asistan Pasif';
                activateBtn.textContent = '🟢 Aktif Et';
                activateBtn.className = 'btn btn-success';
            }
        }

        function toggleVoiceRecognition() {
            if (!recognition) {
                addMessage('❌ Tarayıcınız ses tanımayı desteklemiyor.', 'system');
                showNotification('🚫 Ses tanıma yok!', 'error');
                return;
            }

            if (!isActive) {
                addMessage('❌ Önce asistanı aktif edin!', 'system');
                showNotification('⚠️ Önce aktif edin!', 'warning');
                return;
            }

            if (isListening) {
                stopListening();
            } else {
                startListening();
            }
        }

        function startListening() {
            isListening = true;
            const voiceBtn = document.getElementById('voiceBtn');
            voiceBtn.classList.add('listening');
            voiceBtn.innerHTML = '🔴';
            
            addMessage('🎤 Dinliyorum... Konuşabilirsiniz.', 'system');
            showNotification('🎤 Ses kaydı başladı!', 'info');
            
            try {
                recognition.start();
            } catch (error) {
                stopListening();
                addMessage('❌ Ses tanıma başlatılamadı', 'system');
                showNotification('🚫 Ses tanıma hatası!', 'error');
            }
        }

        function stopListening() {
            isListening = false;
            const voiceBtn = document.getElementById('voiceBtn');
            voiceBtn.classList.remove('listening');
            voiceBtn.innerHTML = '🎤';
            
            if (recognition) {
                try {
                    recognition.stop();
                } catch (error) {
                    console.warn('Recognition stop error:', error);
                }
            }
        }

        async function sendMessage() {
            if (!isActive) {
                addMessage('❌ Asistanı önce aktif edin!', 'system');
                showNotification('⚠️ Asistan pasif!', 'warning');
                return;
            }

            if (!isConnected) {
                addMessage('❌ PC bağlantısı yok!', 'system');
                showNotification('🔴 PC bağlantısı yok!', 'error');
                return;
            }

            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;

            if (!message.startsWith('🎙️')) {
                addMessage(message, 'user');
            }
            
            input.value = '';
            autoResize(input);
            
            showLoading(true);
            
            try {
                await sendToPC(message.replace('🎙️ Sesli komut: "', '').replace('"', ''));
            } catch (error) {
                addMessage(`❌ Hata: ${error.message}`, 'system');
                showNotification('🚫 Mesaj gönderilemedi!', 'error');
            } finally {
                showLoading(false);
            }
        }

        async function sendToPC(message) {
            const serverIP = document.getElementById('serverIP').value || '192.168.1.100';
            const serverPort = document.getElementById('serverPort').value || '5000';

            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 30000);

                const response = await fetch(`http://${serverIP}:${serverPort}/command`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        command: message,
                        mode: currentMode
                    }),
                    signal: controller.signal
                });

                clearTimeout(timeoutId);

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }

                const data = await response.json();
                const reply = data.response?.trim() || 'Komut PC\'ye gönderildi.';
                
                addMessage(reply, 'jarvis');
                
                conversationHistory.push({
                    user: message,
                    jarvis: reply,
                    mode: currentMode,
                    timestamp: new Date().toISOString()
                });

                if (conversationHistory.length > 20) {
                    conversationHistory = conversationHistory.slice(-20);
                }

                // Sesli yanıt
                if ('speechSynthesis' in window && reply.length < 200) {
                    try {
                        speechSynthesis.cancel();
                        
                        const utterance = new SpeechSynthesisUtterance(reply);
                        utterance.lang = 'tr-TR';
                        utterance.rate = 0.85;
                        utterance.pitch = 1.0;
                        utterance.volume = 0.8;
                        
                        const voices = speechSynthesis.getVoices();
                        const turkishVoice = voices.find(voice => 
                            voice.lang.includes('tr') || voice.name.includes('Turkish')
                        );
                        if (turkishVoice) {
                            utterance.voice = turkishVoice;
                        }
                        
                        speechSynthesis.speak(utterance);
                    } catch (speechError) {
                        console.warn('Sesli yanıt hatası:', speechError);
                    }
                }

            } catch (error) {
                if (error.name === 'AbortError') {
                    throw new Error('PC yanıt vermedi (30 saniye)');
                } else {
                    throw new Error(`PC bağlantı hatası: ${error.message}`);
                }
            }
        }

        function quickCommand(command) {
            if (!isActive) {
                if (isConnected) {
                    toggleActivation();
                    setTimeout(() => {
                        if (isActive) {
                            document.getElementById('messageInput').value = command;
                            sendMessage();
                        }
                    }, 1500);
                } else {
                    addMessage('❌ Önce PC bağlantısını test edin!', 'system');
                    showNotification('⚠️ Önce PC\'ye bağlanın!', 'warning');
                }
            } else {
                document.getElementById('messageInput').value = command;
                sendMessage();
            }
        }

        function addMessage(text, sender) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            
            let className = 'message ';
            switch(sender) {
                case 'user':
                    className += 'user-message';
                    break;
                case 'jarvis':
                    className += 'jarvis-message';
                    break;
                case 'system':
                    className += 'system-message';
                    break;
            }
            
            messageDiv.className = className;
            
            const now = new Date();
            const timestamp = now.toLocaleTimeString('tr-TR', { 
                hour: '2-digit', 
                minute: '2-digit',
                second: '2-digit'
            });
            
            if (sender === 'system') {
                messageDiv.innerHTML = `<strong>${text}</strong><br><small style="opacity: 0.6; font-size: 11px;">${timestamp}</small>`;
            } else {
                const senderIcon = sender === 'user' ? '👤' : '🤖';
                messageDiv.innerHTML = `${senderIcon} ${text}<br><small style="opacity: 0.6; font-size: 11px;">${timestamp}</small>`;
            }
            
            chatContainer.appendChild(messageDiv);
            
            setTimeout(() => {
                chatContainer.scrollTo({
                    top: chatContainer.scrollHeight,
                    behavior: 'smooth'
                });
            }, 100);
        }

        function showLoading(show) {
            const loading = document.getElementById('loading');
            loading.style.display = show ? 'block' : 'none';
        }

        function autoResize(textarea) {
            textarea.style.height = 'auto';
            textarea.style.height = Math.min(textarea.scrollHeight, 140) + 'px';
        }

        // Event Listeners
        document.getElementById('messageInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        document.getElementById('messageInput').addEventListener('input', function(e) {
            autoResize(e.target);
        });

        // Sayfa yüklendiğinde
        window.addEventListener('load', function() {
            detectLocalIP();
            
            setTimeout(() => {
                addMessage('🚀 JARVIS Mobil Edition hazır!', 'system');
                addMessage('📱 PC\'nizdeki JARVIS Python kodunuz çalışır durumdayken:', 'system');
                addMessage('🔧 1. PC IP adresinizi girin\n🔗 2. Test butonuna basın\n🟢 3. Aktif Et\'e basın\n💬 4. Sohbet veya Kod modu seçin', 'system');
            }, 1000);

            updateStatus();
            
            if ('speechSynthesis' in window) {
                speechSynthesis.getVoices();
                speechSynthesis.onvoiceschanged = () => {
                    const voices = speechSynthesis.getVoices();
                    console.log('Mevcut sesler:', voices.length);
                };
            }
        });

        // Klavye kısayolları
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                toggleVoiceRecognition();
            }
            
            if (e.ctrlKey && e.key === '/') {
                e.preventDefault();
                quickCommand('Yardım');
            }
            
            if (e.ctrlKey && e.key === 't') {
                e.preventDefault();
                testConnection();
            }
            
            if (e.ctrlKey && e.key === '1') {
                e.preventDefault();
                setMode('chat');
            }
            
            if (e.ctrlKey && e.key === '2') {
                e.preventDefault();
                setMode('code');
            }
            
            if (e.ctrlKey && e.key === ' ') {
                e.preventDefault();
                toggleActivation();
            }
            
            if (e.key === 'Escape' && isListening) {
                e.preventDefault();
                stopListening();
            }
        });

        // Sayfa görünürlük değişikliklerini izle
        document.addEventListener('visibilitychange', function() {
            if (document.hidden) {
                if (isListening) {
                    stopListening();
                }
                if ('speechSynthesis' in window) {
                    speechSynthesis.cancel();
                }
            }
        });

        // Ağ durumunu izle
        window.addEventListener('online', function() {
            showNotification('🌐 İnternet bağlantısı geri geldi!', 'success');
            if (isConnected) {
                setTimeout(testConnection, 1000);
            }
        });

        window.addEventListener('offline', function() {
            showNotification('📡 İnternet bağlantısı kesildi!', 'error');
            updateConnectionStatus(false);
        });

        // Hata yakalama
        window.addEventListener('error', function(e) {
            console.error('Global hata:', e.error);
            showNotification('⚠️ Bir hata oluştu!', 'error');
        });

        window.addEventListener('unhandledrejection', function(e) {
            console.error('Promise hatası:', e.reason);
            showNotification('🚫 Bağlantı hatası!', 'error');
        });

        window.addEventListener('beforeunload', function() {
            if (isListening) {
                stopListening();
            }
            if ('speechSynthesis' in window) {
                speechSynthesis.cancel();
            }
        });
    </script>
</body>
</html>
