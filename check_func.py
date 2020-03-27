from pydub import AudioSegment

def check_extension(file_path, extension = ".mp3"):
        """(bool)Checks if file is of a certain extension | string file_path, extensiom"""
        isExtension = (file_path.lower()).endswith(extension.lower())
        return isExtension

def check_duration(audio_segment,min_dur = 0,  max_dur = 3600):
        """(bool)Checks if audio durations is in desired range | AudioSegment audio_segment; int min_dur, max_dur"""
        inRange =  max_dur > audio_segment.duration_seconds > min_dur
        return inRange

def check_peaking(audio_segment,slice_interval = 10000, max_peaks = 10):
        """(bool)Checks if audio is withing peaking restrictions, based on audio segments | AudioSegment audio_segment; int slice_itnerval, max_peaks"""
        slices = audio_segment[::slice_interval]
        count = 0
        for i in slices:
                count += (i.max_dBFS == 0)
        isPeaking = count > max_peaks
        return  isPeaking
def check_normalization(audio_segment, normalize_threshold = -1):
        """(bool)Checks if audio is normalize above a certain threshold | AudioSegment audio_segment; int normalize_threshold"""
        isNormalized = (audio_segment.max_dBFS >= normalize_threshold)
        return isNormalized

def check_volume(audio_segment, volume_threshold = -3):
        """(bool)Chek if audio has loudness above certaqin threshold | AudioSegment audio_segment; int volume_threshold"""
        isLoud =  (audio_segment.dBFS >= volume_threshold)
        return isLoud

