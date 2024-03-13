import pygame
import sys

def run_game():
    # Pygameの初期化
    pygame.init()

    # ゲームウィンドウの設定
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("不思議のダンジョン")

    # ゲームループのフラグ
    running = True

    # ゲームのメインループ
    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 画面を黒でクリア
        screen.fill((0, 0, 0))

        # ここでゲームオブジェクトを更新・描画

        # 画面を更新
        pygame.display.flip()

        # FPS制御
        pygame.time.Clock().tick(60)

    # Pygameの終了処理
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    run_game()
