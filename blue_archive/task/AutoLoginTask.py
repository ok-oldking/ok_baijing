from cv2.typing import MatLike
from typing_extensions import override

from autoui.scene.Scene import Scene
from autoui.task.FindFeatureTask import FindFindFeatureTask
from autoui.task.TaskExecutor import TaskExecutor
from blue_archive.scene.StartScence import StartScene


class AutoLoginTask(FindFindFeatureTask):

    @override
    def run_frame(self, executor: TaskExecutor, scene: Scene, frame: MatLike):
        if isinstance(scene, StartScene):
            print(f"Start scene click")
            executor.click_relative(0.5, 0.5)
            executor.sleep(1)
