<!-- <script lang="ts">
  import { onMount } from "svelte";

  let videoSource: HTMLVideoElement | null = null;
  let capturedImage: string | null = null;

  async function obtenerVideoCamara() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      //@ts-ignore
      videoSource.srcObject = stream;
      //@ts-ignore
      videoSource.play();
    } catch (error) {
      console.error(error);
    }
  }
  async function analyzeImage() {
    takeImage();

    if (capturedImage) {
      try {
        const response = await fetch(
          "https://prodeh.pythonanywhere.com/computer-vision",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
              Origin: window.location.origin,
            },
            body: JSON.stringify({
              Image: capturedImage,
            }),
          }
        );
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        console.log(result);
        // Handle the API response here
      } catch (error) {
        console.error(error);
      }
    }
  }
  async function takeImage() {
    if (videoSource) {
      const canvas = document.createElement("canvas");
      canvas.width = videoSource.videoWidth;
      canvas.height = videoSource.videoHeight;
      canvas.getContext("2d")?.drawImage(videoSource, 0, 0);
      capturedImage = canvas.toDataURL("image/jpeg");
      return capturedImage;
    }
  }

  onMount(async () => {
    obtenerVideoCamara();

    try {
      const response = await fetch("/api/computer-vision", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const result = await response.json();
      console.log(result);
      // Handle the API response here
    } catch (error) {
      console.error(error);
    }
  });
</script>
-->

<script>
  let videoSource;
  function analyzeImage() {}
</script>

<div class="vido">
  <div class="video-feed">
    <video bind:this={videoSource}><track kind="captions" /></video>
  </div>
  <button class="btn bg-primary mt-4 ml-2" on:click={analyzeImage}
    >Analyze</button
  >
  <!-- {#if capturedImage}
    <img src={capturedImage} alt="Captured" />
  {/if} -->
</div>
